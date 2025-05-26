#!/usr/bin/env python3
"""
MCPM - The MCP Package Manager
"The package manager that manages package managers"
Inspired by apt, cargo, and nix - but for MCP servers.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcpm")

# The registry of power
REGISTRY_URL = "https://raw.githubusercontent.com/modelcontextprotocol/servers/main/servers.json"
MCPM_HOME = Path.home() / ".mcpm"
INSTALLED_DB = MCPM_HOME / "installed.json"
CACHE_DIR = MCPM_HOME / "cache"

class MCPPackageManager:
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.registry: Dict[str, Any] = {}
        self.installed: Dict[str, Any] = {}
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Create the sacred directories"""
        MCPM_HOME.mkdir(exist_ok=True)
        CACHE_DIR.mkdir(exist_ok=True)
        if not INSTALLED_DB.exists():
            INSTALLED_DB.write_text("{}")

    async def _load_installed(self):
        """Load the tome of installed servers"""
        try:
            self.installed = json.loads(INSTALLED_DB.read_text())
        except:
            self.installed = {}

    async def _save_installed(self):
        """Persist the installation state"""
        INSTALLED_DB.write_text(json.dumps(self.installed, indent=2))

    async def _fetch_registry(self):
        """Fetch the registry of all MCP servers"""
        if not self.session:
            self.session = aiohttp.ClientSession()
        async with self.session.get(REGISTRY_URL) as resp:
            data = await resp.json()
            self.registry = {s["id"]: s for s in data["servers"]}

    async def list_available(self) -> List[Dict[str, Any]]:
        """List all servers in the multiverse"""
        await self._fetch_registry()
        return [{"name": k, "description": v.get("description", ""),
                "installed": k in self.installed} for k, v in self.registry.items()]

    async def search(self, query: str) -> List[Dict[str, Any]]:
        """Search the cosmic registry"""
        await self._fetch_registry()
        query = query.lower()
        results = []
        for name, server in self.registry.items():
            if query in name.lower() or query in server.get("description", "").lower():
                results.append({"name": name, "description": server.get("description", "")})
        return results

    async def install(self, name: str) -> Dict[str, Any]:
        """Install a server from the void"""
        await self._fetch_registry()
        await self._load_installed()

        if name not in self.registry:
            return {"error": f"Server '{name}' not found in registry"}

        if name in self.installed:
            return {"error": f"Server '{name}' already installed"}

        server = self.registry[name]

        # Determine installation method
        if "npm" in server:
            result = await self._install_npm(name, server["npm"])
        elif "docker" in server:
            result = await self._install_docker(name, server["docker"])
        elif "git" in server:
            result = await self._install_git(name, server["git"])
        else:
            return {"error": f"No installation method found for '{name}'"}

        if "error" not in result:
            self.installed[name] = {"method": result["method"], "details": result}
            await self._save_installed()

        return result

    async def _install_npm(self, name: str, package: str) -> Dict[str, Any]:
        """Channel the npm spirits"""
        try:
            proc = await asyncio.create_subprocess_exec(
                "npm", "install", "-g", package,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            if proc.returncode == 0:
                return {"method": "npm", "package": package, "status": "installed"}
            return {"error": stderr.decode()}
        except Exception as e:
            return {"error": str(e)}

    async def _install_docker(self, name: str, image: str) -> Dict[str, Any]:
        """Summon the container daemon"""
        try:
            proc = await asyncio.create_subprocess_exec(
                "docker", "pull", image,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            if proc.returncode == 0:
                return {"method": "docker", "image": image, "status": "pulled"}
            return {"error": stderr.decode()}
        except Exception as e:
            return {"error": str(e)}

    async def _install_git(self, name: str, repo: str) -> Dict[str, Any]:
        """Clone from the source"""
        target = MCPM_HOME / "repos" / name
        target.parent.mkdir(exist_ok=True)
        try:
            proc = await asyncio.create_subprocess_exec(
                "git", "clone", repo, str(target),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            if proc.returncode == 0:
                return {"method": "git", "repo": repo, "path": str(target), "status": "cloned"}
            return {"error": stderr.decode()}
        except Exception as e:
            return {"error": str(e)}

    async def uninstall(self, name: str) -> Dict[str, Any]:
        """Banish a server back to the void"""
        await self._load_installed()

        if name not in self.installed:
            return {"error": f"Server '{name}' not installed"}

        info = self.installed[name]

        # Clean up based on installation method
        if info["method"] == "git" and "path" in info["details"]:
            path = Path(info["details"]["path"])
            if path.exists():
                import shutil
                shutil.rmtree(path)

        del self.installed[name]
        await self._save_installed()
        return {"status": "uninstalled", "name": name}

    async def list_installed(self) -> List[Dict[str, Any]]:
        """Show the chosen ones"""
        await self._load_installed()
        return [{"name": k, **v} for k, v in self.installed.items()]

    async def cleanup(self):
        """Release resources"""
        if self.session:
            await self.session.close()

# MCP Server Interface
async def handle_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """The grand dispatcher"""
    mcpm = MCPPackageManager()

    try:
        method = request.get("method", "")
        params = request.get("params", {})

        if method == "tools/list":
            return {
                "tools": [
                    {"name": "list", "description": "List all available MCP servers"},
                    {"name": "search", "description": "Search for MCP servers"},
                    {"name": "install", "description": "Install an MCP server"},
                    {"name": "uninstall", "description": "Remove an installed server"},
                    {"name": "installed", "description": "List installed servers"}
                ]
            }

        elif method == "tools/call":
            tool = params.get("name")
            args = params.get("arguments", {})

            if tool == "list":
                result = await mcpm.list_available()
            elif tool == "search":
                result = await mcpm.search(args.get("query", ""))
            elif tool == "install":
                result = await mcpm.install(args.get("name", ""))
            elif tool == "uninstall":
                result = await mcpm.uninstall(args.get("name", ""))
            elif tool == "installed":
                result = await mcpm.list_installed()
            else:
                result = {"error": f"Unknown tool: {tool}"}

            return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}

    finally:
        await mcpm.cleanup()

    return {"error": {"code": -32601, "message": "Method not found"}}

async def main():
    """The eternal loop"""
    logger.info("MCPM awakens...")

    async for line in async_stdin():
        try:
            request = json.loads(line)
            response = await handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()
        except Exception as e:
            logger.error(f"Error: {e}")

async def async_stdin():
    """Async stdin reader"""
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)

    while True:
        line = await reader.readline()
        if not line:
            break
        yield line.decode().strip()

if __name__ == "__main__":
    asyncio.run(main())

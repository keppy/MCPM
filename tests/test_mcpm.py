#!/usr/bin/env python3
"""
Tests for MCPM - The MCP Package Manager

Copyright 2024 James Dominguez
Licensed under the Apache License, Version 2.0
"""

import pytest
import json
import subprocess
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock
import sys
import os
import shutil

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcpm import MCPPackageManager, handle_request


@pytest.fixture
async def mcpm():
    """Create a test instance of MCPPackageManager"""
    manager = MCPPackageManager()
    # Use a temporary directory for testing
    manager.MCPM_HOME = Path("/tmp/test_mcpm")
    manager.INSTALLED_DB = manager.MCPM_HOME / "installed.json"
    manager.CACHE_DIR = manager.MCPM_HOME / "cache"
    manager._ensure_dirs()
    yield manager
    # Cleanup
    if manager.session:
        await manager.cleanup()


@pytest.mark.asyncio
async def test_list_tools():
    """Test that tool listing works correctly"""
    response = await handle_request({"method": "tools/list"})
    assert "tools" in response
    tools = response["tools"]
    assert len(tools) == 5
    tool_names = {tool["name"] for tool in tools}
    assert tool_names == {"list", "search", "install", "uninstall", "installed"}


@pytest.mark.asyncio
async def test_search_functionality(mcpm):
    """Test search functionality"""
    # Mock registry
    mcpm.registry = {
        "test-server": {"description": "A test MCP server"},
        "another-server": {"description": "Another server for testing"},
        "database-tool": {"description": "Database management MCP"}
    }

    results = await mcpm.search("test")
    assert len(results) == 2
    assert any(r["name"] == "test-server" for r in results)
    assert any(r["name"] == "another-server" for r in results)


@pytest.mark.asyncio
async def test_install_npm_package(mcpm):
    """Test npm package installation"""
    mcpm.registry = {
        "test-package": {"npm": "@test/package", "description": "Test package"}
    }

    with patch("asyncio.create_subprocess_exec") as mock_exec:
        mock_process = AsyncMock()
        mock_process.communicate = AsyncMock(return_value=(b"", b""))
        mock_process.returncode = 0
        mock_exec.return_value = mock_process

        result = await mcpm.install("test-package")

        assert result["method"] == "npm"
        assert result["package"] == "@test/package"
        assert result["status"] == "installed"
        mock_exec.assert_called_once_with(
            "npm", "install", "-g", "@test/package",
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )


@pytest.mark.asyncio
async def test_install_already_installed(mcpm):
    """Test installing an already installed package"""
    mcpm.installed = {"existing-package": {"method": "npm", "details": {}}}
    mcpm.registry = {"existing-package": {"npm": "@existing/package"}}

    result = await mcpm.install("existing-package")
    assert "error" in result
    assert "already installed" in result["error"]


@pytest.mark.asyncio
async def test_uninstall_package(mcpm):
    """Test package uninstallation"""
    # Setup installed package
    mcpm.installed = {
        "test-package": {
            "method": "git",
            "details": {"path": "/tmp/test_mcpm/repos/test-package"}
        }
    }

    with patch("shutil.rmtree") as mock_rmtree:
        result = await mcpm.uninstall("test-package")

        assert result["status"] == "uninstalled"
        assert result["name"] == "test-package"
        assert "test-package" not in mcpm.installed


@pytest.mark.asyncio
async def test_list_installed_empty(mcpm):
    """Test listing installed packages when none are installed"""
    mcpm.installed = {}
    result = await mcpm.list_installed()
    assert result == []


@pytest.mark.asyncio
async def test_registry_fetch_error(mcpm):
    """Test handling of registry fetch errors"""
    with patch("aiohttp.ClientSession.get") as mock_get:
        mock_get.side_effect = Exception("Network error")

        with pytest.raises(Exception):
            await mcpm._fetch_registry()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

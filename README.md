# MCPM - The MCP Package Manager

> "The package manager that manages package managers"

MCPM is an MCP server that installs and manages other MCP servers. It's the meta-package manager for the Model Context Protocol ecosystem.

## Features

- 📦 **Registry-based**: Pulls from the official MCP servers registry
- 🚀 **Multi-method installation**: Supports npm, Docker, and git
- 💾 **Persistent state**: Tracks installed servers
- 🔍 **Search**: Find servers by name or description
- ⚡ **Async**: Built for performance
- 🔧 **Simple**: Under 200 lines of code

## Installation

### Using npm (recommended)
```bash
npm install -g @mcp/mcpm
```

### Using uv (for development)
```bash
git clone https://github.com/your-org/mcpm.git
cd mcpm
uv pip install -e .
```

## Configuration

Add MCPM to your MCP settings:

```json
{
  "mcpm": {
    "command": "npx",
    "args": ["-y", "@mcp/mcpm"]
  }
}
```

Or if installed globally:

```json
{
  "mcpm": {
    "command": "mcpm"
  }
}
```

## Usage

MCPM provides the following tools:

### `list`
List all available MCP servers in the registry.

### `search`
Search for MCP servers by name or description.
- **Arguments**: `query` (string) - Search term

### `install`
Install an MCP server from the registry.
- **Arguments**: `name` (string) - Server name

### `uninstall`
Remove an installed MCP server.
- **Arguments**: `name` (string) - Server name

### `installed`
List all currently installed MCP servers.

## Example Usage with Claude

```
Human: Use mcpm to search for database servers
Assistant: I'll search for database-related MCP servers...

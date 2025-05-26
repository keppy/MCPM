## Example Usage with Claude

```
Human: Use mcpm to search for database servers
Assistant: I'll search for database-related MCP servers...# MCPM - The MCP Package Manager

> "The package manager that manages package managers"

MCPM is an MCP server that installs and manages other MCP servers. It's the meta-package manager for the Model Context Protocol ecosystem.

## Features

- 📦 **Registry-based**: Pulls from the official MCP servers registry
- 🚀 **Multi-method installation**: Supports npm, Docker, and git
- 💾 **Persistent state**: Tracks installed servers
- 🔍 **Search**: Find servers by name or description
- ⚡ **Async**: Built for performance
- 🔧 **Simple**: Under 200 lines of code
- 🏠 **Isolated**: Uses its own virtual environment

## Installation

### Using npm (recommended)
```bash
npm install -g @keppylab/mcpm
```

The npm package will automatically:
1. Create a virtual environment at `~/.mcpm/venv`
2. Install Python dependencies (aiohttp)
3. Set up the `mcpm` command

### For Development

Using uv (fastest):
```bash
git clone https://github.com/keppy/mcpm.git
cd mcpm
chmod +x dev.sh
./dev.sh
source .venv/bin/activate
```

Using pip:
```bash
git clone https://github.com/keppy/mcpm.git
cd mcpm
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Configuration

Add MCPM to your MCP settings:

```json
{
  "mcpm": {
    "command": "npx",
    "args": ["-y", "@keppylab/mcpm"]
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

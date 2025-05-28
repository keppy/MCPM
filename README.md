<h1 align="center">
  <br>
  <img src="./logo.svg#gh-light-mode-only" width="160" alt="MCPM">
  <img src="./logo-dark.svg#gh-dark-mode-only" width="160" alt="MCPM">
  <br>
  <sub>Speak Systems Into Existence</sub>
  <br>
  <br>
  <a href="https://www.npmjs.com/package/@keppylab/mcpm">
    <img src="https://img.shields.io/npm/v/@keppylab/mcpm.svg" alt="npm version">
  </a>
  <a href="https://github.com/keppy/mcpm/blob/main/LICENSE">
    <img src="https://img.shields.io/npm/l/@keppylab/mcpm.svg" alt="license">
  </a>
  <a href="https://nodejs.org">
    <img src="https://img.shields.io/node/v/@keppylab/mcpm.svg" alt="node version">
  </a>
</h1>

Watch me build a complete RAG system in 7 prompts:

```
1. "Find me filesystem and database servers"
2. "Install them"
3. "Create an embedding schema"
4. "Read my documents"
5. "Index them"
6. "Make it searchable"
7. "Give me a terminal interface"
```

**Result**: Working RAG system. No config files. No documentation. Just conversation.

## What Is This?

MCPM transforms infrastructure from something you configure to something you converse with. It's a package manager for MCP servers, but that's like saying a compiler is a text processor.

What it really does: **Makes infrastructure disappear into natural language.**

### The Old Way (Hours)
1. Read MCP server documentation
2. Figure out installation methods
3. Manually edit JSON configs
4. Debug path issues
5. Restart Claude Desktop repeatedly
6. Pray it works

### The MCPM Way (Minutes)
1. Tell Claude what you want
2. It happens
3. You use it

## See It In Action

### Build a GitHub PR Analyzer (5 prompts)
```
"Install github and code-analysis servers"
"Connect to my repo"
"Analyze open PRs for complexity"
"Flag potential issues"
"Show me the results"
```
**Result**: PR analysis bot running.

### Create a SQL Natural Language Interface (4 prompts)
```
"Install sqlite server"
"Connect to my database"
"Let me query it in plain English"
"Show results as tables"
```
**Result**: Chat with your database.

### Turn CSVs into an API (6 prompts)
```
"Install filesystem and data servers"
"Read all CSVs from ~/data"
"Create REST endpoints for each"
"Add search functionality"
"Add JSON export"
"Start the server"
```
**Result**: Your spreadsheets are now an API.

## Quick Start (2 minutes)

<img src="https://img.shields.io/badge/$ mcpm-Install%20Now-0a0a0a?style=for-the-badge&labelColor=0a0a0a&color=6366f1&logo=terminal" alt="Install MCPM">

```bash
# Install MCPM
npm install -g @keppylab/mcpm

# Add to Claude Desktop config
{
  "mcpm": {
    "command": "npx",
    "args": ["-y", "@keppylab/mcpm"]
  }
}

# Restart Claude Desktop
# Start speaking systems into existence
```

## The Paradigm Shift

**Traditional Programming**: Learn syntax → Write code → Debug → Deploy

**Conversational Infrastructure**: Describe what you want → Get it running → Iterate by talking

This isn't just about saving time. It's about who can build systems. With MCPM:
- A researcher can build a knowledge base
- A designer can create data pipelines  
- A student can build analysis tools

Because the barrier isn't syntax anymore. It's imagination.

## How It Works

MCPM is an MCP server that manages other MCP servers. When you say "install filesystem server", it:

1. Searches the official MCP registry
2. Installs the server (npm, Docker, or git)
3. Configures it in your MCP client
4. Makes it available to Claude

But you don't need to know any of that. You just need to know what you want to build.

## Available Commands

### Conversational Mode (Recommended)
When using MCPM through Claude Desktop, just describe what you want:

| What You Say | What Happens |
|--------------|--------------|
| "Search for database servers" | Shows available database MCP servers |
| "Install server-name" | Installs and configures the server |
| "Show installed servers" | Lists what you have |
| "Remove server-name" | Uninstalls cleanly |
| "Backup my config" | Saves your setup |

### Direct CLI Mode
MCPM also provides a direct command-line interface for power users:

```bash
# Package Management
mcpm list                    # List all available MCP servers
mcpm search <query>          # Search servers by name/description
mcpm install <server>        # Install an MCP server
mcpm uninstall <server>      # Remove an installed server
mcpm installed               # Show installed servers

# Configuration Management
mcpm config-add <server>     # Add installed server to MCP config
mcpm config-remove <server>  # Remove server from config
mcpm config-list             # List configured servers
mcpm config-backup           # Backup current configuration
mcpm config-restore <file>   # Restore from backup
```

**Examples:**
```bash
mcpm search filesystem       # Find file-related servers
mcpm install postgres        # Install PostgreSQL server
mcpm config-add postgres     # Add to MCP configuration
mcpm config-list             # Verify it's configured
```

## Real Examples

### The 7-Prompt RAG System
See [EXAMPLE.md](EXAMPLE.md) for the complete walkthrough. From zero to a working document Q&A system in under 10 minutes.

### Infrastructure as Conversation
```
Human: My RAG system is too slow
Claude: I see it's scanning all documents on each query. Let me add caching...
*modifies the running system*
Claude: Try now - should be 10x faster
```

The system can see its own state and modify itself through conversation.

## Technical Details

**For those who care about the internals:**

- Written in Python with async/await
- Uses the official MCP server registry
- Supports npm, Docker, and git installations
- Automatic config discovery across platforms
- Isolated virtual environment prevents conflicts
- Full backup/restore capabilities

**Requirements:**
- Python 3.9+
- Node.js 18+
- Claude Desktop or compatible MCP client

## Installation Options

### Quick (Recommended)
```bash
npm install -g @keppylab/mcpm
```

### From Source
```bash
git clone https://github.com/keppy/mcpm.git
cd mcpm
./dev.sh  # or python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Platform Support

MCPM automatically finds your MCP config on:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

## The Philosophy

We're not building better tools. We're removing the need to think about tools at all.

MCPM is part of a larger vision where infrastructure becomes conversational. Where the gap between thought and running system approaches zero.

This is just the beginning.

## Join the Revolution

- **GitHub**: [keppy/mcpm](https://github.com/keppy/mcpm)
- **Twitter**: [@keppylab_ai](https://twitter.com/keppylab_ai)
- **Discord**: [Join our community](https://discord.gg/6rd4M4e4hT)

Built with ❤️  and a healthy disrespect for configuration files.

---

*"The best interface is no interface. The best configuration is conversation."*

## License

Apache-2.0 - Because infrastructure should be free to speak.

## Status

🚀 **v0.1.3** - Config management, backup/restore, platform detection
🔮 **Coming Soon** - Version management, dependency resolution, health checks

---

**Ready to speak your first system into existence?** [Get started →](#quick-start-2-minutes)

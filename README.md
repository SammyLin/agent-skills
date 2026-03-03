# Agent Skills

A collection of micro-skills organized by action-based categories for AI agents (Claude Code, etc.).

See [PRINCIPLES.md](./PRINCIPLES.md) for design principles and conventions.

## Categories

| Category | Skills | Description |
|----------|--------|-------------|
| **generate/** | 14 | Content & document creation (PDF, DOCX, PPTX, XLSX, design, etc.) |
| **scaffold/** | 4 | Project scaffolding & templates (FastAPI, MCP server, web artifacts) |
| **develop/** | 4 | Development workflows & tools (git, n8n, uv, product dev) |
| **check/** | 2 | Testing & validation (webapp testing, product health check) |
| **track/** | 3 | Project management (Linear CLI, Linear workflow, product planning) |
| **search/** | 4 | Search & research (Twitter, web search, skill discovery) |
| **transcribe/** | 2 | Audio/video transcription (YouTube, MLX Whisper) |
| **deploy/** | 1 | Deployment (Cloudflare) |
| **knowledge/** | 1 | Knowledge management (Obsidian) |
| **notify/** | 1 | Notifications (completion notifier) |
| **query/** | 1 | Data queries (Taiwan stock) |
| **review/** | 1 | Code review |

## All Skills

### generate/
- `algorithmic-art` - Generate algorithmic art with JavaScript
- `autocomplete-component` - Build autocomplete UI components
- `canvas-design` - Design with HTML Canvas
- `doc-coauthoring` - Co-author documents
- `docx` - Generate Word documents
- `frontend-design` - Design frontend interfaces
- `image-gen-workflow` - Image generation workflow
- `internal-comms` - Internal communications drafting
- `line-sticker-processor` - Process LINE stickers
- `pdf` - Generate and manipulate PDFs
- `pptx` - Generate PowerPoint presentations
- `slack-gif-creator` - Create Slack GIFs
- `theme-factory` - Generate design themes
- `xlsx` - Generate Excel spreadsheets

### scaffold/
- `fastapi-generator` - Scaffold FastAPI projects
- `mcp-builder` - Build MCP servers
- `skill-creator` - Create new skills
- `web-artifacts-builder` - Build web artifacts

### develop/
- `git-commit-helper` - Git commit assistance
- `n8n-node-configuration` - Configure n8n nodes
- `product-dev-workflow` - Product development workflow
- `uv-package-manager` - Python uv package manager

### check/
- `product-health-check` - Product health monitoring
- `webapp-testing` - Web application testing

### track/
- `linear-cli` - Linear CLI commands
- `linear-workflow` - Linear GraphQL API workflow
- `product-planning` - Product planning

### search/
- `agent-browser-twitter` - Search Twitter via browser agent
- `find-skills` - Discover available skills
- `research-workflow` - Research workflow
- `tavily-search` - Web search via Tavily API

### transcribe/
- `mlx-whisper` - Local audio transcription with MLX Whisper
- `youtube` - YouTube transcript extraction

### deploy/
- `cloudflare` - Deploy to Cloudflare

### knowledge/
- Obsidian knowledge management workflow

### notify/
- `completion-notifier` - Task completion notifications

### query/
- `tw-stock` - Taiwan stock market queries

### review/
- `code-review-workflow` - Code review workflow

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md      # Required: name + description + instructions
├── scripts/      # Optional: executable scripts
├── references/   # Optional: documentation
└── assets/       # Optional: templates, resources
```

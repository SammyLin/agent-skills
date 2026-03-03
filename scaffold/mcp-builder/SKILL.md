---
name: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). Do not use for: using existing MCP tools, building REST APIs without MCP, general backend development, or Claude skill creation (use skill-creator).
license: Complete terms in LICENSE.txt
---

# MCP Server Development Guide

## Overview

Create MCP servers that enable LLMs to interact with external services through well-designed tools. Quality is measured by how well it enables LLMs to accomplish real-world tasks.

## High-Level Workflow

### Phase 1: Deep Research and Planning

1. **Understand Modern MCP Design**: Balance API coverage vs workflow tools. Use clear naming, concise descriptions, actionable errors.
2. **Study MCP Protocol**: Start with `https://modelcontextprotocol.io/sitemap.xml`, fetch pages with `.md` suffix.
3. **Study Framework Docs**:
   - [MCP Best Practices](./references/reference/mcp_best_practices.md)
   - **TypeScript (recommended)**: Fetch SDK README from GitHub, see [TypeScript Guide](./references/reference/node_mcp_server.md)
   - **Python**: Fetch SDK README from GitHub, see [Python Guide](./references/reference/python_mcp_server.md)
4. **Plan Implementation**: Review API docs, prioritize comprehensive endpoint coverage.

### Phase 2: Implementation

1. **Set Up Project** - See language-specific guides
2. **Core Infrastructure** - API client, error handling, response formatting, pagination
3. **Implement Tools** - For each tool:
   - Input schema (Zod/Pydantic with constraints and descriptions)
   - Output schema (define `outputSchema` where possible)
   - Tool description (concise summary, parameter descriptions)
   - Async/await, error handling, pagination support
   - Annotations: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`

### Phase 3: Review and Test

- No duplicated code, consistent error handling, full type coverage, clear descriptions
- **TypeScript**: `npm run build`, test with MCP Inspector
- **Python**: `python -m py_compile`, test with MCP Inspector

### Phase 4: Create Evaluations

Load [Evaluation Guide](./references/reference/evaluation.md) for complete guidelines.

1. Inspect tools, explore available data with READ-ONLY operations
2. Create 10 complex, realistic, independent, read-only, verifiable, stable questions
3. Verify answers yourself
4. Output XML file with `<evaluation>` / `<qa_pair>` / `<question>` / `<answer>` structure

## Reference Files

- [MCP Best Practices](./references/reference/mcp_best_practices.md) - Universal guidelines
- [Python Guide](./references/reference/python_mcp_server.md) - FastMCP patterns
- [TypeScript Guide](./references/reference/node_mcp_server.md) - MCP SDK patterns
- [Evaluation Guide](./references/reference/evaluation.md) - Testing guidelines
- **MCP Protocol**: `https://modelcontextprotocol.io/sitemap.xml`
- **Python SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

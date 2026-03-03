---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. Do not use for: finding/installing existing skills (use find-skills), building MCP servers (use mcp-builder), or general documentation writing.
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. They transform Claude from a general-purpose agent into a specialized agent equipped with procedural knowledge.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. **Default assumption: Claude is already very smart.** Only add context Claude doesn't already have. Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

- **High freedom**: Multiple approaches valid, decisions depend on context
- **Medium freedom**: Preferred pattern exists, some variation acceptable
- **Low freedom**: Operations are fragile, consistency critical, specific sequence required

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name + description, required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code
    ├── references/       - Documentation loaded as needed
    └── assets/           - Files used in output
```

### Progressive Disclosure

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude

Keep SKILL.md body under 500 lines. Split content into separate files when approaching this limit.

## Skill Creation Process

1. **Understand** the skill with concrete examples
2. **Plan** reusable skill contents (scripts, references, assets)
3. **Initialize** the skill: `scripts/init_skill.py <skill-name> --path <output-directory>`
4. **Edit** the skill (implement resources and write SKILL.md)
5. **Package** the skill: `scripts/package_skill.py <path/to/skill-folder>`
6. **Iterate** based on real usage

### SKILL.md Frontmatter

- `name`: The skill name
- `description`: Primary triggering mechanism. Include what the skill does AND when to use it. Include all "when to use" info here (not in body).

### SKILL.md Body

Write instructions using imperative/infinitive form. Include information beneficial and non-obvious to Claude.

## Detailed Reference

For bundled resource details (scripts/, references/, assets/), progressive disclosure patterns, detailed creation steps, and examples, see [references/templates-and-examples.md](references/templates-and-examples.md).

Consult these guides based on needs:
- **Multi-step processes**: See references/workflows.md for sequential workflows
- **Output formats/quality standards**: See references/output-patterns.md

# Skill Creator: Templates and Examples

## Bundled Resources Reference

### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without reading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

### References (`references/`)

Documentation and reference material intended to be loaded as needed into context.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/api_docs.md` for API specs
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both

### Assets (`assets/`)

Files not intended to be loaded into context, used within the output Claude produces.

- **When to include**: When the skill needs files used in final output
- **Examples**: `assets/logo.png`, `assets/slides.pptx`, `assets/frontend-template/`, `assets/font.ttf`
- **Benefits**: Separates output resources from documentation

### What NOT to Include

Do NOT create extraneous documentation:
- README.md, INSTALLATION_GUIDE.md, QUICK_REFERENCE.md, CHANGELOG.md, etc.
- The skill should only contain information needed for an AI agent to do the job

## Progressive Disclosure Patterns

Keep SKILL.md body under 500 lines. Split content when approaching this limit. Always reference split files from SKILL.md.

**Key principle:** When a skill supports multiple variations, keep only core workflow and selection guidance in SKILL.md. Move variant-specific details into separate reference files.

### Pattern 1: High-level guide with references

```markdown
# PDF Processing

## Quick start
Extract text with pdfplumber:
[code example]

## Advanced features
- **Form filling**: See [FORMS.md](FORMS.md) for complete guide
- **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
```

### Pattern 2: Domain-specific organization

```
bigquery-skill/
SKILL.md (overview and navigation)
reference/
    finance.md (revenue, billing metrics)
    sales.md (opportunities, pipeline)
    product.md (API usage, features)
    marketing.md (campaigns, attribution)
```

When user asks about sales metrics, Claude only reads sales.md.

For skills supporting multiple frameworks:
```
cloud-deploy/
SKILL.md (workflow + provider selection)
references/
    aws.md (AWS deployment patterns)
    gcp.md (GCP deployment patterns)
    azure.md (Azure deployment patterns)
```

### Pattern 3: Conditional details

```markdown
# DOCX Processing

## Creating documents
Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents
For simple edits, modify XML directly.
**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

**Important guidelines:**
- Avoid deeply nested references - keep one level deep from SKILL.md
- Structure longer reference files (>100 lines) with a table of contents

## Skill Creation Process: Detailed Steps

### Step 1: Understanding with Concrete Examples

Ask questions like:
- "What functionality should the skill support?"
- "Can you give examples of how this skill would be used?"
- "What would a user say that should trigger this skill?"

Avoid too many questions in a single message. Conclude when there's a clear sense of needed functionality.

### Step 2: Planning Reusable Contents

Analyze each example by:
1. Considering how to execute from scratch
2. Identifying what scripts, references, and assets would be helpful

Examples:
- `pdf-editor` skill: "Rotate this PDF" -> `scripts/rotate_pdf.py`
- `frontend-webapp-builder` skill: "Build me a todo app" -> `assets/hello-world/` template
- `big-query` skill: "How many users logged in today?" -> `references/schema.md`

### Step 3: Initializing the Skill

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

The script:
- Creates skill directory at specified path
- Generates SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, `assets/`
- Adds example files that can be customized or deleted

### Step 4: Editing the Skill

#### Learn Design Patterns

Consult guides based on needs:
- **Multi-step processes**: See references/workflows.md
- **Output formats/quality standards**: See references/output-patterns.md

#### Start with Reusable Contents

Begin with `scripts/`, `references/`, `assets/` files. May require user input (e.g., brand assets, documentation).

Added scripts must be tested by actually running them. Delete unneeded example files.

#### Update SKILL.md

**Writing Guidelines:** Always use imperative/infinitive form.

##### Frontmatter
- `name`: The skill name
- `description`: Primary triggering mechanism. Include what the skill does AND when to use it. Include all "when to use" info here (not in body). Example: "Comprehensive document creation, editing, and analysis... Use when Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content..."

Do not include any other fields in YAML frontmatter.

### Step 5: Packaging

```bash
scripts/package_skill.py <path/to/skill-folder>
# Optional output directory:
scripts/package_skill.py <path/to/skill-folder> ./dist
```

The script will:
1. **Validate**: YAML frontmatter, naming conventions, description quality, file organization
2. **Package**: Creates .skill file (zip with .skill extension) if validation passes

### Step 6: Iterate

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or resources should be updated
4. Implement changes and test again

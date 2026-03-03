---
name: pptx
description: "Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for: (1) Creating new presentations, (2) Modifying or editing content, (3) Working with layouts, (4) Adding comments or speaker notes, or any other presentation tasks. Do not use for: Google Slides, Keynote files, PDF slide decks, or creating presentation content without .pptx output."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX creation, editing, and analysis

## Overview

A .pptx file is a ZIP archive containing XML files and resources. Different workflows apply for reading, creating, and editing.

## Reading and analyzing content

### Text extraction
```bash
python -m markitdown path-to-file.pptx
```

### Raw XML access
For comments, speaker notes, layouts, animations, design elements, and complex formatting, unpack the file:
```bash
python ooxml/scripts/unpack.py <office_file> <output_dir>
```

**Note**: The unpack.py script is at `skills/pptx/ooxml/scripts/unpack.py`. If not found, use `find . -name "unpack.py"`.

## Creating a new presentation (without template)

Use the **html2pptx** workflow.

### Design Principles

**CRITICAL**: Before creating, analyze content and choose appropriate design elements:
1. Consider subject matter, tone, industry, mood
2. Check for branding (company/organization)
3. Match palette to content
4. State your approach before writing code

**Requirements**:
- State content-informed design approach BEFORE writing code
- Use web-safe fonts only: Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, Tahoma, Trebuchet MS, Impact
- Create clear visual hierarchy; ensure readability; be consistent

**Layout Tips**: For slides with charts/tables, use two-column layout (preferred) or full-slide layout. NEVER vertically stack charts/tables below text.

For color palettes and visual detail options, see [references/ooxml-reference.md](references/ooxml-reference.md).

### Workflow
1. **MANDATORY**: Read [`html2pptx.md`](html2pptx.md) completely (no range limits)
2. Create HTML file per slide (720pt x 405pt for 16:9). Use `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>`. Use `class="placeholder"` for chart/table areas. Rasterize gradients/icons as PNG first using Sharp.
3. Run JavaScript using [`html2pptx.js`](scripts/html2pptx.js) to convert HTML to PowerPoint
4. **Visual validation**: `python scripts/thumbnail.py output.pptx workspace/thumbnails --cols 4` - check for text cutoff, overlap, positioning, contrast issues. Fix and regenerate if needed.

## Editing an existing presentation

### Workflow
1. **MANDATORY**: Read [`ooxml.md`](ooxml.md) completely (~500 lines, no range limits)
2. Unpack: `python ooxml/scripts/unpack.py <office_file> <output_dir>`
3. Edit XML files (primarily `ppt/slides/slide{N}.xml`)
4. **CRITICAL**: Validate after each edit: `python ooxml/scripts/validate.py <dir> --original <file>`
5. Pack: `python ooxml/scripts/pack.py <input_directory> <office_file>`

## Creating a presentation (using template)

### Workflow
1. Extract text and create thumbnails: `python -m markitdown template.pptx > template-content.md` and `python scripts/thumbnail.py template.pptx`
2. Analyze template and save inventory to `template-inventory.md` (0-indexed slides)
3. Create outline with template mapping in `outline.md`. Match layout structure to content.
4. Rearrange slides: `python scripts/rearrange.py template.pptx working.pptx 0,34,34,50,52`
5. Extract text inventory: `python scripts/inventory.py working.pptx text-inventory.json`. Read full file.
6. Generate replacement JSON and save to `replacement-text.json`. ALL shapes cleared unless "paragraphs" provided.
7. Apply: `python scripts/replace.py working.pptx replacement-text.json output.pptx`

For detailed JSON structure, formatting rules, and template workflow specifics, see [references/ooxml-reference.md](references/ooxml-reference.md).

## Code Style Guidelines
Write concise code. Avoid verbose variable names, redundant operations, and unnecessary print statements.

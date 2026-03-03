# OOXML Reference for PowerPoint

Detailed reference for OOXML file structure, template-based workflows, and editing guidelines.

## Key File Structures

* `ppt/presentation.xml` - Main presentation metadata and slide references
* `ppt/slides/slide{N}.xml` - Individual slide contents (slide1.xml, slide2.xml, etc.)
* `ppt/notesSlides/notesSlide{N}.xml` - Speaker notes for each slide
* `ppt/comments/modernComment_*.xml` - Comments for specific slides
* `ppt/slideLayouts/` - Layout templates for slides
* `ppt/slideMasters/` - Master slide templates
* `ppt/theme/` - Theme and styling information
* `ppt/media/` - Images and other media files

## Typography and Color Extraction

**When given an example design to emulate**: Always analyze the presentation's typography and colors first:
1. **Read theme file**: Check `ppt/theme/theme1.xml` for colors (`<a:clrScheme>`) and fonts (`<a:fontScheme>`)
2. **Sample slide content**: Examine `ppt/slides/slide1.xml` for actual font usage (`<a:rPr>`) and colors
3. **Search for patterns**: Use grep to find color (`<a:solidFill>`, `<a:srgbClr>`) and font references across all XML files

## Design Principles for New Presentations (without template)

### Color Palette Selection

**Choosing colors creatively**:
- Think beyond defaults - match colors to the specific topic
- Consider: topic, industry, mood, energy level, target audience, brand identity
- Build palette: 3-5 colors (dominant + supporting + accent)
- Ensure text contrast on backgrounds

**Example palettes** (use to spark creativity):
1. **Classic Blue**: #1C2833, #2E4053, #AAB7B8, #F4F6F6
2. **Teal & Coral**: #5EA8A7, #277884, #FE4447, #FFFFFF
3. **Bold Red**: #C0392B, #E74C3C, #F39C12, #F1C40F, #2ECC71
4. **Warm Blush**: #A49393, #EED6D3, #E8B4B8, #FAF7F2
5. **Burgundy Luxury**: #5D1D2E, #951233, #C15937, #997929
6. **Deep Purple & Emerald**: #B165FB, #181B24, #40695B, #FFFFFF
7. **Cream & Forest Green**: #FFE1C7, #40695B, #FCFCFC
8. **Pink & Purple**: #F8275B, #FF574A, #FF737D, #3D2F68
9. **Lime & Plum**: #C5DE82, #7C3A5F, #FD8C6E, #98ACB5
10. **Black & Gold**: #BF9A4A, #000000, #F4F6F6
11. **Sage & Terracotta**: #87A96B, #E07A5F, #F4F1DE, #2C2C2C
12. **Charcoal & Red**: #292929, #E33737, #CCCBCB
13. **Vibrant Orange**: #F96D00, #F2F2F2, #222831
14. **Forest Green**: #191A19, #4E9F3D, #1E5128, #FFFFFF
15. **Retro Rainbow**: #722880, #D72D51, #EB5C18, #F08800, #DEB600
16. **Vintage Earthy**: #E3B448, #CBD18F, #3A6B35, #F4F1DE
17. **Coastal Rose**: #AD7670, #B49886, #F3ECDC, #BFD5BE
18. **Orange & Turquoise**: #FC993E, #667C6F, #FCFCFC

### Visual Details Options

**Geometric Patterns**: Diagonal dividers, asymmetric columns (30/70, 40/60), rotated text, circular/hexagonal frames, triangular accents, overlapping shapes

**Border & Frame Treatments**: Thick single-side borders, double-line borders, corner brackets, L-shaped borders, underline accents

**Typography Treatments**: Extreme size contrast, all-caps with letter spacing, oversized section numbers, monospace for data, condensed fonts for dense info, outlined text

**Chart & Data Styling**: Monochrome charts with accent color, horizontal bars, dot plots, minimal gridlines, data labels directly on elements, oversized key metrics

**Layout Innovations**: Full-bleed images with overlays, sidebar columns, modular grids, Z/F-pattern flow, floating text boxes, magazine-style layouts

**Background Treatments**: Solid color blocks (40-60% of slide), gradient fills, split backgrounds, edge-to-edge color bands, negative space

## Template-Based Workflow Details

### Template Analysis (Step 2)

Create and save a template inventory file at `template-inventory.md` containing:
```markdown
# Template Inventory Analysis
**Total Slides: [count]**
**IMPORTANT: Slides are 0-indexed (first slide = 0, last slide = count-1)**

## [Category Name]
- Slide 0: [Layout code if available] - Description/purpose
- Slide 1: [Layout code] - Description/purpose
[... EVERY slide must be listed individually with its index ...]
```

### Outline Creation (Step 3)

**CRITICAL: Match layout structure to actual content**:
- Single-column layouts: Use for unified narrative or single topic
- Two-column layouts: Use ONLY when you have exactly 2 distinct items/concepts
- Three-column layouts: Use ONLY when you have exactly 3 distinct items/concepts
- Image + text layouts: Use ONLY when you have actual images to insert
- Quote layouts: Use ONLY for actual quotes from people (with attribution)
- Never use layouts with more placeholders than you have content
- Count your actual content pieces BEFORE selecting the layout

Example template mapping:
```
template_mapping = [
    0,   # Use slide 0 (Title/Cover)
    34,  # Use slide 34 (B1: Title and body)
    34,  # Use slide 34 again (duplicate for second B1)
    50,  # Use slide 50 (E1: Quote)
    54,  # Use slide 54 (F2: Closing + Text)
]
```

### Text Inventory JSON Structure (Step 5)

```json
{
  "slide-0": {
    "shape-0": {
      "placeholder_type": "TITLE",
      "left": 1.5,
      "top": 2.0,
      "width": 7.5,
      "height": 1.2,
      "paragraphs": [
        {
          "text": "Paragraph text",
          "bullet": true,
          "level": 0,
          "alignment": "CENTER",
          "space_before": 10.0,
          "space_after": 6.0,
          "line_spacing": 22.4,
          "font_name": "Arial",
          "font_size": 14.0,
          "bold": true,
          "italic": false,
          "underline": false,
          "color": "FF0000"
        }
      ]
    }
  }
}
```

Key features:
- Slides named "slide-0", "slide-1", etc.
- Shapes ordered by visual position as "shape-0", "shape-1", etc.
- Placeholder types: TITLE, CENTER_TITLE, SUBTITLE, BODY, OBJECT, or null
- Default font size from layout placeholders when available
- Slide numbers filtered automatically
- Bullets: when `bullet: true`, `level` is always included
- Only non-default values included in output

### Replacement JSON (Step 6)

**CRITICAL rules**:
- First verify which shapes exist in the inventory
- The replace.py script validates all shapes exist
- ALL text shapes from inventory are cleared unless you provide "paragraphs"
- Paragraphs with bullets are automatically left aligned
- When bullet: true, do NOT include bullet symbols in text
- Headers/titles should have `"bold": true`
- List items should have `"bullet": true, "level": 0`

Example paragraphs field:
```json
"paragraphs": [
  { "text": "Title", "alignment": "CENTER", "bold": true },
  { "text": "Header", "bold": true },
  { "text": "Bullet point", "bullet": true, "level": 0 },
  { "text": "Red text", "color": "FF0000" },
  { "text": "Theme text", "theme_color": "DARK_1" },
  { "text": "Regular text" }
]
```

## Thumbnail Grid Creation

```bash
python scripts/thumbnail.py template.pptx [output_prefix]
```

Features:
- Creates: `thumbnails.jpg` (or numbered for large decks)
- Default: 5 columns, max 30 slides per grid
- Custom prefix: `python scripts/thumbnail.py template.pptx my-grid`
- Adjust columns: `--cols 4` (range: 3-6)
- Grid limits: 3 cols = 12, 4 cols = 20, 5 cols = 30, 6 cols = 42
- Slides are zero-indexed

## Converting Slides to Images

```bash
# Convert PPTX to PDF
soffice --headless --convert-to pdf template.pptx

# Convert PDF pages to JPEG
pdftoppm -jpeg -r 150 template.pdf slide
# Options: -f N (first page), -l N (last page), -png for PNG
```

## Dependencies

- **markitdown**: `pip install "markitdown[pptx]"` (text extraction)
- **pptxgenjs**: `npm install -g pptxgenjs` (creating via html2pptx)
- **playwright**: `npm install -g playwright` (HTML rendering)
- **react-icons**: `npm install -g react-icons react react-dom`
- **sharp**: `npm install -g sharp` (SVG rasterization)
- **LibreOffice**: `sudo apt-get install libreoffice` (PDF conversion)
- **Poppler**: `sudo apt-get install poppler-utils` (pdftoppm)
- **defusedxml**: `pip install defusedxml` (secure XML parsing)

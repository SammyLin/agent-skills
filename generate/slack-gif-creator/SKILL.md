---
name: slack-gif-creator
description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack." Do not use for: video creation, static image design, non-Slack platforms with different size constraints, or editing existing GIFs.
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator

A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack.

## Slack Requirements

**Dimensions:** Emoji GIFs: 128x128 (recommended), Message GIFs: 480x480

**Parameters:** FPS: 10-30, Colors: 48-128, Duration: under 3 seconds for emoji GIFs

## Core Workflow

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

builder = GIFBuilder(width=128, height=128, fps=10)

for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)
    # Draw animation using PIL primitives
    builder.add_frame(frame)

builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Working with User-Uploaded Images

If a user uploads an image, determine if they want to use it directly or as inspiration:
```python
uploaded = Image.open('file.png')
```

## Drawing from Scratch

Use PIL ImageDraw primitives: `draw.ellipse()`, `draw.polygon()`, `draw.line()`, `draw.rectangle()`.

**Don't use:** Emoji fonts (unreliable) or assume pre-packaged graphics exist.

## Philosophy

This skill provides knowledge (Slack requirements, animation concepts), utilities (GIFBuilder, validators, easing), and flexibility (create logic with PIL primitives). It does NOT provide rigid templates, emoji fonts, or pre-packaged graphics.

Be creative! Combine concepts and use PIL's full capabilities.

## Dependencies

```bash
pip install pillow imageio numpy
```

## Detailed Reference

For complete API reference (GIFBuilder, validators, easing functions, frame helpers), animation concepts (shake, pulse, bounce, spin, fade, slide, zoom, explode), optimization strategies, and graphics tips, see [references/api-and-animation-reference.md](references/api-and-animation-reference.md).

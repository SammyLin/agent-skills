---
name: algorithmic-art
description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations. Do not use for: static image design (use canvas-design instead), photo editing, non-interactive illustrations, or 3D rendering.
license: Complete terms in LICENSE.txt
---

Algorithmic philosophies are computational aesthetic movements expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms).

This happens in two steps:
1. Algorithmic Philosophy Creation (.md file)
2. Express by creating p5.js generative art (.html + .js files)

## ALGORITHMIC PHILOSOPHY CREATION

Create an ALGORITHMIC PHILOSOPHY (not static images) interpreted through computational processes, emergent behavior, seeded randomness, noise fields, particles, flows, and parametric variation.

### THE CRITICAL UNDERSTANDING
- What is received: Subtle user input as foundation, not constraint
- What is created: An algorithmic philosophy/generative aesthetic movement
- What happens next: The philosophy is EXPRESSED IN CODE - p5.js sketches that are 90% algorithmic generation, 10% essential parameters

### HOW TO GENERATE

**Name the movement** (1-2 words): e.g., "Organic Turbulence" / "Quantum Harmonics"

**Articulate the philosophy** (4-6 paragraphs): Express how it manifests through computational processes, noise functions, particle behaviors, temporal evolution, parametric variation.

**CRITICAL GUIDELINES:**
- Avoid redundancy - each concept mentioned once
- Emphasize craftsmanship REPEATEDLY: "meticulously crafted," "deep computational expertise," "master-level implementation"
- Leave creative space for interpretive implementation

### ESSENTIAL PRINCIPLES
- **ALGORITHMIC PHILOSOPHY**: Computational worldview expressed through code
- **PROCESS OVER PRODUCT**: Beauty emerges from algorithm execution - each run unique
- **PARAMETRIC EXPRESSION**: Ideas through math, forces, behaviors - not static composition
- **PURE GENERATIVE ART**: LIVING ALGORITHMS, not static images with randomness
- **EXPERT CRAFTSMANSHIP**: Must feel meticulously crafted by a master

Output the philosophy as a .md file (4-6 paragraphs).

## P5.JS IMPLEMENTATION

### STEP 0: READ THE TEMPLATE FIRST

**CRITICAL: BEFORE writing any HTML:**
1. **Read** `templates/viewer.html` using the Read tool
2. **Use that file as the LITERAL STARTING POINT**
3. **Keep all FIXED sections** (header, sidebar structure, Anthropic colors/fonts, seed controls, action buttons)
4. **Replace only VARIABLE sections** (algorithm, parameters, UI controls)

### CRAFTSMANSHIP REQUIREMENTS

- **Balance**: Complexity without noise, order without rigidity
- **Color Harmony**: Thoughtful palettes, not random RGB
- **Composition**: Visual hierarchy even in randomness
- **Performance**: Smooth execution
- **Reproducibility**: Same seed = identical output

### OUTPUT FORMAT

1. **Algorithmic Philosophy** - Markdown explaining the generative aesthetic
2. **Single HTML Artifact** - Self-contained interactive art built from `templates/viewer.html`

For philosophy examples, conceptual seed deduction, technical requirements, parameter structure, artifact details, and interactive viewer reference, see [references/philosophy-and-patterns.md](references/philosophy-and-patterns.md).

## RESOURCES

- **templates/viewer.html**: REQUIRED STARTING POINT for all HTML artifacts
- **templates/generator_template.js**: Reference for p5.js best practices

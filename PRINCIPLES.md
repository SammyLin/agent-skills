# Micro-Skill Principles

## 1. Micro-Skill Architecture
- Like Micro-Services
- Small, independent, reusable components
- Don't repeat - call existing skills instead

## 2. Sensitive Data Isolation
- Never put secrets in SKILL.md
- Use environment variables or external config files

## 3. Prefer Building, Use External Judiciously
- Prioritize using our own skills
- Only use external skills for non-core functionality

## 4. Precise Description
- Clearly state when to use
- Clearly state when NOT to use
- Include keywords for AI matching
- Example: `"Use for: Taiwan stock quotes. Do not use for: crypto, US stocks."`

## 5. Progressive Disclosure
- Load metadata first (name, description)
- Load full SKILL.md only when actually used
- Saves tokens, improves performance

## 6. Skill Structure
```
skill-name/
├── SKILL.md      # Required: name + description + instructions
├── scripts/      # Optional: executable scripts
├── references/   # Optional: documentation
└── assets/       # Optional: templates, resources
```

## 7. Skill Usage Tracking
- Log each skill usage
- Review usage every 2 days
- Consider deleting or merging unused skills

## 8. Organize by Action/Function, Not Domain
- **DO:** Name by what it DOES (twitter-search, stock-query, code-review)
- **DON'T:** Name by category (search, transcription, finance)
- Skills often span domains - action-based naming is more intuitive
- Example: OpenAI organizes as "transcribe", "imagegen", "vercel-deploy"

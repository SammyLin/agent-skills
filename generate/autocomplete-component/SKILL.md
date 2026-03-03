---
name: autocomplete-component
description: Generate Alpine.js + TailwindCSS autocomplete dropdowns for search inputs. Use when building search features for stocks, cities, products, users, or any searchable data. Supports dark/light themes, API/JSON/static data sources, and customizable fields. Saves ~7k tokens by providing production-ready autocomplete UI instead of writing from scratch each time. Do not use for: React/Vue/Svelte components, full-page search UIs, backend search logic, or non-dropdown UI patterns (tables, lists, filters).
---

# Autocomplete Component Generator

Generate professional autocomplete dropdowns with Alpine.js and TailwindCSS.

## What You Get

- **Alpine.js component** - Reactive, lightweight (no build step)
- **TailwindCSS styled** - Dark/light themes included
- **Multiple data sources** - API, JSON file, or static array
- **Customizable fields** - Map your data structure
- **Keyboard accessible** - Focus, blur, selection
- **Production-ready** - Used in real projects

## Quick Start

### Basic Usage (Dark Theme, API Data Source)

```bash
python scripts/generate_autocomplete.py autocomplete.html
```

Generates a component that:
- Calls `/api/items/search?q={query}`
- Displays `name` and `description` fields
- Dark theme styling
- Emits `item-selected` event

### Stock Search Example

```bash
python scripts/generate_autocomplete.py stock-autocomplete.html \
  --theme dark \
  --api-endpoint /api/stocks/search \
  --id-field code \
  --primary-field code \
  --secondary-field name \
  --label "股票代碼" \
  --placeholder "例如：2330、台積電"
```

### City Search (Light Theme, JSON File)

```bash
python scripts/generate_autocomplete.py city-autocomplete.html \
  --theme light \
  --data-source json \
  --label "Select City"
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `output_file` | *required* | Output HTML file path |
| `--theme` | `dark` | UI theme (`dark` or `light`) |
| `--data-source` | `api` | Data source (`api`, `json`, `static`) |
| `--api-endpoint` | `/api/items/search` | API endpoint path |
| `--id-field` | `id` | Unique identifier field |
| `--primary-field` | `name` | Main display field (highlighted) |
| `--secondary-field` | `description` | Secondary display field |
| `--label` | `Search` | Input label text |
| `--placeholder` | `Type to search...` | Input placeholder |
| `--component-id` | `1` | Component ID (for multiple instances) |

## Data Source Options

### API (Default)
- Best for: Database queries, large datasets
- Requires: Backend API endpoint
- Example: `/api/stocks/search?q=2330`

### JSON File
- Best for: Static reference data (countries, categories)
- Requires: JSON file at `/data/items.json`
- Loads once, filters client-side

### Static Array
- Best for: Small, fixed options (<100 items)
- Requires: Manual data editing in generated HTML
- No external dependencies

## Integration

### Step 1: Generate Component

```bash
python scripts/generate_autocomplete.py autocomplete.html --theme dark
```

### Step 2: Include in Your Page

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <!-- Include generated component -->
    <div>
        <!-- Paste autocomplete.html content here -->
    </div>
</body>
</html>
```

### Step 3: Handle Selection

**Method 1: Alpine.js Event**

```html
<div @item-selected="handleSelection($event.detail)">
    <!-- autocomplete component -->
</div>

<script>
function app() {
    return {
        handleSelection(item) {
            console.log('Selected:', item);
        }
    }
}
</script>
```

**Method 2: Global Callback**

```javascript
window.on1Select = function(item) {
    console.log('Selected:', item);
    document.getElementById('result').value = item.id;
};
```

## API Endpoint Template

Use `assets/autocomplete-api-template.py` to create your backend:

```python
@router.get("/api/stocks/search")
async def search_stocks(q: str = ""):
    stocks = load_stocks()
    
    if not q:
        return stocks[:10]
    
    q = q.strip().lower()
    matches = [s for s in stocks if q in s['code'].lower() or q in s['name'].lower()]
    
    return matches[:10]
```

## Multiple Autocomplete on Same Page

```bash
# First autocomplete
python scripts/generate_autocomplete.py stock.html --component-id Stock

# Second autocomplete  
python scripts/generate_autocomplete.py city.html --component-id City
```

Each gets unique:
- Function: `autocompleteStock()`, `autocompleteCity()`
- Callback: `window.onStockSelect()`, `window.onCitySelect()`

## When to Use

Use this skill when:

- Building search features (stocks, products, users, cities)
- Need autocomplete/typeahead functionality
- Want to avoid writing Alpine.js boilerplate
- Need both dark and light theme options
- Working with FastAPI or similar backend

## Customization

For advanced customization, see:

- `references/examples.md` - Real-world usage examples
- `references/customization.md` - Theme, field mapping, UI tweaks

Common customizations:
- Dropdown height: Change `max-h-64` class
- Display template: Edit HTML structure in generated file
- Search behavior: Modify `search()` function logic
- Styling: Adjust TailwindCSS classes

## Token Savings

Estimated **~7k tokens saved** per use by providing:
- Complete Alpine.js autocomplete logic
- TailwindCSS dark/light theme styling
- Multiple data source implementations
- Customizable field mappings
- Production-ready accessibility features

Instead of describing requirements and debugging Alpine.js reactivity issues, use this skill to generate working code instantly.

# Autocomplete Component Examples

## 範例 1: 股票搜尋（API 資料源）

```bash
python scripts/generate_autocomplete.py stock-autocomplete.html \
  --theme dark \
  --data-source api \
  --api-endpoint /api/stocks/search \
  --id-field code \
  --primary-field code \
  --secondary-field name \
  --label "股票代碼" \
  --placeholder "例如：2330、台積電" \
  --help-text "💡 支援台股代碼或股名搜尋"
```

**對應的 API 端點：**

```python
@router.get("/stocks/search")
async def search_stocks(q: str = ""):
    stocks = load_stocks_from_db()
    
    if not q:
        return stocks[:10]
    
    q = q.strip().lower()
    matches = []
    
    for stock in stocks:
        if stock['code'].lower().startswith(q):
            matches.append({**stock, "priority": 1})
        elif q in stock['name'].lower():
            matches.append({**stock, "priority": 2})
    
    matches.sort(key=lambda x: x['priority'])
    return [m for m in matches][:10]
```

---

## 範例 2: 城市搜尋（JSON 檔案資料源）

```bash
python scripts/generate_autocomplete.py city-autocomplete.html \
  --theme light \
  --data-source json \
  --id-field id \
  --primary-field name \
  --secondary-field country \
  --label "Select City" \
  --placeholder "Start typing city name..."
```

**對應的 JSON 檔案** (`/data/cities.json`):

```json
[
  {
    "id": 1,
    "name": "Tokyo",
    "country": "Japan",
    "population": "37.4M"
  },
  {
    "id": 2,
    "name": "New York",
    "country": "United States",
    "population": "8.3M"
  }
]
```

---

## 範例 3: 產品搜尋（靜態資料）

```bash
python scripts/generate_autocomplete.py product-autocomplete.html \
  --theme dark \
  --data-source static \
  --id-field sku \
  --primary-field name \
  --secondary-field category \
  --label "Search Products" \
  --placeholder "Product name or category..."
```

生成後，在 HTML 中手動替換靜態資料：

```javascript
const allItems = [
    { sku: 'PROD-001', name: 'Laptop', category: 'Electronics', price: '$999' },
    { sku: 'PROD-002', name: 'Mouse', category: 'Accessories', price: '$29' },
    // ... more items
];
```

---

## 範例 4: 多個自動補完（同一頁面）

```bash
# 第一個：股票搜尋
python scripts/generate_autocomplete.py stock-search.html \
  --component-id Stock \
  --api-endpoint /api/stocks/search

# 第二個：城市搜尋
python scripts/generate_autocomplete.py city-search.html \
  --component-id City \
  --api-endpoint /api/cities/search
```

每個元件會有獨立的：
- 函式名稱：`autocompleteStock()`, `autocompleteCity()`
- 事件處理：`window.onStockSelect()`, `window.onCitySelect()`

---

## 範例 5: 整合到 FastAPI 專案

**Step 1: 生成元件**

```bash
python scripts/generate_autocomplete.py autocomplete.html \
  --theme dark \
  --api-endpoint /api/items/search
```

**Step 2: 複製到 templates 目錄**

```bash
# 將生成的 HTML 片段加入到你的主模板中
cat autocomplete.html >> templates/index.html
```

**Step 3: 加入 API 端點**

使用 `assets/autocomplete-api-template.py` 作為範本，建立你的 API。

---

## 事件處理範例

### 方法 1: Alpine.js 事件監聽

```html
<div @item-selected="handleSelection($event.detail)">
    <!-- Autocomplete component here -->
</div>

<script>
function myApp() {
    return {
        handleSelection(item) {
            console.log('Selected:', item);
            // Do something with the selected item
        }
    }
}
</script>
```

### 方法 2: 全域回調函式

```javascript
window.on1Select = function(item) {
    console.log('Selected:', item);
    // Do something with the selected item
    document.getElementById('result').textContent = item.name;
};
```

---

## 自訂樣式範例

生成後，你可以進一步自訂 CSS：

```css
/* 自訂下拉選單高度 */
.autocomplete-scrollbar-dark {
    max-height: 400px !important;
}

/* 自訂項目 hover 效果 */
.hover\\:bg-slate-700:hover {
    background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
}
```

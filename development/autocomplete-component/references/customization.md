# Autocomplete Customization Guide

## 主題自訂

### Dark Theme (預設)
- 深色背景：`bg-slate-700`, `bg-slate-800`
- 深色邊框：`border-slate-600`, `border-slate-700`
- 主要顏色：`text-teal-400`
- 適合深色儀表板、管理面板

### Light Theme
- 淺色背景：`bg-white`
- 淺色邊框：`border-gray-300`
- 主要顏色：`text-blue-600`
- 適合一般網站、表單

### 建立自訂主題

編輯 `generate_autocomplete.py` 並新增主題配置：

```python
THEMES = {
    'custom': {
        'LABEL_COLOR': 'text-purple-700',
        'INPUT_BG': 'bg-purple-50',
        'INPUT_BORDER': 'border-purple-300',
        'DROPDOWN_BG': 'bg-purple-100',
        'HOVER_BG': 'hover:bg-purple-200',
        'HIGHLIGHT_COLOR': 'text-purple-600',
        # ... more colors
    }
}
```

---

## 資料來源自訂

### API 資料源

**優點：**
- 動態資料
- 支援大量資料集
- 伺服器端搜尋和過濾

**適用場景：**
- 資料庫查詢
- 即時資料
- 大型資料集（>1000 筆）

**範例：**
```bash
--data-source api --api-endpoint /api/stocks/search
```

### JSON 檔案資料源

**優點：**
- 簡單易用
- 適合中型資料集
- 可快取

**適用場景：**
- 靜態參考資料（國家、城市、類別）
- 中型資料集（100-1000 筆）

**範例：**
```bash
--data-source json
```

**需要：** 建立 `/data/items.json` 檔案

### 靜態陣列資料源

**優點：**
- 最簡單
- 無需額外檔案或 API
- 適合小型資料集

**適用場景：**
- 固定選項（狀態、分類）
- 小型資料集（<100 筆）

**範例：**
```bash
--data-source static
```

**需要：** 手動編輯生成的 HTML，替換靜態資料陣列

---

## 欄位映射

### 預設欄位結構

```json
{
  "id": 1,
  "name": "Item Name",
  "description": "Item Description"
}
```

### 自訂欄位映射

#### 股票資料範例

資料結構：
```json
{
  "code": "2330",
  "name": "台積電",
  "fullName": "台灣積體電路製造股份有限公司",
  "category": "半導體",
  "market": "上市"
}
```

欄位映射：
```bash
--id-field code \
--primary-field code \
--secondary-field name
```

顯示結果：
- **2330** 台積電
- 台灣積體電路製造股份有限公司 · 半導體

#### 使用者資料範例

資料結構：
```json
{
  "userId": "user123",
  "email": "user@example.com",
  "displayName": "John Doe",
  "role": "Admin"
}
```

欄位映射：
```bash
--id-field userId \
--primary-field email \
--secondary-field displayName
```

---

## 搜尋行為自訂

### 最小搜尋長度

```bash
--min-search-length 2  # 至少輸入 2 個字元才開始搜尋
```

適合：
- 大型資料集（減少不必要的請求）
- 中文搜尋（通常至少 2 個字）

### API 端點參數

預設：`?q={query}`

自訂 API 參數名稱（需手動修改生成的 HTML）：

```javascript
// 原始
const response = await fetch(`/api/items/search?q=${encodeURIComponent(value)}`);

// 改為
const response = await fetch(`/api/items/search?query=${encodeURIComponent(value)}`);
```

---

## UI 自訂

### 下拉選單高度

預設：`max-h-64`（256px）

自訂：編輯生成的 HTML

```html
<!-- 原始 -->
<div class="... max-h-64 overflow-y-auto">

<!-- 改為 400px -->
<div class="... max-h-96 overflow-y-auto">
```

### 項目顯示模板

預設顯示：
```
[Primary] [Secondary]
[Tertiary] · [Category]     [Meta]
```

自訂（編輯生成的 HTML）：

```html
<div class="flex items-center justify-between">
    <div class="flex-1">
        <!-- 自訂顯示 -->
        <div class="text-sm font-medium text-slate-100">
            <span class="text-teal-400" x-text="item.code"></span>
            <span x-text="item.name"></span>
            <span class="ml-2 text-xs bg-teal-600 px-2 py-0.5 rounded" x-text="item.market"></span>
        </div>
        <div class="text-xs text-slate-400 mt-0.5" x-text="item.category"></div>
    </div>
    <div class="text-xs text-slate-500" x-text="'$' + item.price"></div>
</div>
```

### 圖示和徽章

加入圖示：

```html
<span class="text-teal-400">
    📊 <span x-text="item.code"></span>
</span>
```

加入徽章：

```html
<span 
    x-show="item.isNew"
    class="ml-2 text-xs bg-green-600 px-2 py-0.5 rounded">
    NEW
</span>
```

---

## 進階功能

### 多選模式

將 `select()` 函式改為累加而非替換：

```javascript
select(item) {
    // 原始：單選
    this.query = item.name;
    
    // 改為：多選（需額外的 selectedItems 陣列）
    if (!this.selectedItems) {
        this.selectedItems = [];
    }
    
    this.selectedItems.push(item);
    this.query = '';  // 清空輸入框
    this.showDropdown = false;
}
```

### 鍵盤導航

加入上下鍵選擇：

```javascript
highlightedIndex: -1,

handleKeyDown(event) {
    if (event.key === 'ArrowDown') {
        this.highlightedIndex = Math.min(this.highlightedIndex + 1, this.suggestions.length - 1);
        event.preventDefault();
    } else if (event.key === 'ArrowUp') {
        this.highlightedIndex = Math.max(this.highlightedIndex - 1, 0);
        event.preventDefault();
    } else if (event.key === 'Enter' && this.highlightedIndex >= 0) {
        this.select(this.suggestions[this.highlightedIndex]);
        event.preventDefault();
    }
}
```

並在 input 加上：

```html
<input @keydown="handleKeyDown($event)" ...>
```

### 快取搜尋結果

```javascript
searchCache: {},

async search(value) {
    // 檢查快取
    if (this.searchCache[value]) {
        this.suggestions = this.searchCache[value];
        return;
    }
    
    // 執行搜尋
    const response = await fetch(`/api/items/search?q=${encodeURIComponent(value)}`);
    const results = await response.json();
    
    // 存入快取
    this.searchCache[value] = results;
    this.suggestions = results;
}
```

---

## 整合範例

### 整合到表單

```html
<form x-data="{ formData: { itemId: null } }">
    
    <!-- Autocomplete -->
    <div @item-selected="formData.itemId = $event.detail.id">
        <!-- Include autocomplete component here -->
    </div>
    
    <!-- Other form fields -->
    <input type="hidden" name="item_id" x-model="formData.itemId">
    
    <button type="submit">Submit</button>
</form>
```

### 與其他 UI 元件搭配

```html
<!-- 顯示已選擇的項目 -->
<div x-data="{ selectedItem: null }" @item-selected="selectedItem = $event.detail">
    
    <!-- Autocomplete -->
    <div><!-- ... --></div>
    
    <!-- Selected item display -->
    <div x-show="selectedItem" class="mt-4 p-4 bg-green-100 rounded">
        <p>You selected: <strong x-text="selectedItem?.name"></strong></p>
        <button @click="selectedItem = null">Clear</button>
    </div>
</div>
```

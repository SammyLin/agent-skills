---
name: research-workflow
description: 網路研究與資訊收集流程。當需要搜尋網路、收集資訊、整理研究結果時使用。根據資料類型選擇最適合的工具：輕量查詢用 web_search，需要網頁內容用 web_fetch，需要操作網頁用 agent-browser 或 browser。Do not use for: 本地檔案搜尋、代碼庫搜尋（用 grep/glob）、Twitter 搜尋（用 agent-browser-twitter）、或資料庫查詢。
---

# Research Workflow

## 工具選擇優先順序

### 1. web_search（最快）
- 用於：快速關鍵字搜尋、新聞、價格查詢
- API：Brave Search
- 範例：
```bash
web_search(query="bitcoin price", count=5, freshness="pd")
web_search(query="AI news", count=10)
```

### 2. web_fetch（輕量）
- 用於：取得網頁內容（文章、文件）
- 範例：
```bash
web_fetch(url="https://example.com/article", maxChars=5000)
```

### 3. agent-browser（推薦）
- 用於：需要互動的網頁操作（登入、填表、點擊）
- 特色：用 accessibility refs 操作，比 CSS selector 穩定
- 範例：
```bash
agent-browser open <url>
agent-browser snapshot       # 拿頁面結構 (refs: @e1, @e2...)
agent-browser click @e2
agent-browser fill @e3 "text"
```

### 4. browser（最後手段）
- 用於：需要完整 JS 渲染的複雜網頁
- 最重最慢

## 搜尋技巧

### Twitter/X 搜尋
永遠用 bird skill：
```bash
bird search "關鍵字" -n 10
bird user-tweets @handle
```
認證設定：`~/.config/bird/credentials.json`

### 一般網頁搜尋
用 web_search，支援參數：
- `country`: 國家代碼（TW, US 等）
- `freshness`: pd（一週內）、pw（一月內）、pm（一月內）
- `search_lang`: 語言

## 研究流程

1. **定義問題** - 清楚知道要找什麼
2. **選擇工具** - 根據場景選最適合的
3. **執行搜尋** - 1-3 次搜尋取得足夠資訊
4. **整理結果** - 濃縮成重點
5. **提供建議** - 基於研究結果給出結論

## 常見場景

| 場景 | 工具 | 範例查詢 |
|------|------|----------|
| 價格查詢 | web_search | "bitcoin ethereum price" |
| 新聞資訊 | web_search | "AI news today" |
| 產品資訊 | web_fetch | Elecrow 產品頁面 |
| 價格比較 | web_search | "CrowPanel ESP32 price" |
| 技術文件 | web_fetch | Wiki 文件 |
| 社群討論 | bird | Twitter 關鍵字 |

## 輸出格式

研究結果用簡潔格式呈現：
- 標題 + 來源連結
- 的重點（3-5 點）
- 建議或結論

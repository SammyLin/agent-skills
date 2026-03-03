---
name: tw-stock
description: 查詢台股即時報價、歷史數據。支援 Fugle API（主要）和 Shioaji（備援）兩個資料源互相備援。Do not use for: 加密貨幣、美股/港股/其他非台灣市場、股票交易下單、技術分析圖表生成、或財務報表分析。
---

# 台股查價 Skill

查詢台灣股票即時報價，支援兩個 API 互相備援。

## 資料源

| 優先順序 | API | 用途 | 環境變數 |
|---------|-----|------|---------|
| 1（主要）| Fugle | RESTful，快速簡單 | `FUGLE_API_KEY` |
| 2（備援）| Shioaji | 永豐券商 API，功能完整 | `SINOTRADE_API_KEY` + `SINOTRADE_SECRET_KEY` |

## 常用股票代碼

| 代碼 | 名稱 | | 代碼 | 名稱 |
|------|------|-|------|------|
| 2330 | 台積電 | | 2317 | 鴻海 |
| 2308 | 台達電 | | 2454 | 聯發科 |
| 2881 | 富邦金 | | 2882 | 國泰金 |
| 2412 | 中華電 | | 0050 | 元大台灣50 |
| 0056 | 元大高股息 | | 00878 | 國泰永續高股息 |

## 方法 1：Fugle API（推薦）

### 即時報價
```bash
source ~/.zshrc
curl -s "https://api.fugle.tw/marketdata/v1.0/stock/intraday/quote/{股票代碼}" \
  -H "X-API-KEY: $FUGLE_API_KEY" | python3 -m json.tool
```

### 回傳欄位說明
- `lastPrice` - 最新成交價
- `openPrice` - 開盤價
- `highPrice` - 最高價
- `lowPrice` - 最低價
- `closePrice` - 收盤價（盤中為最新價）
- `previousClose` / `referencePrice` - 昨收/參考價
- `change` - 漲跌
- `changePercent` - 漲跌幅 %
- `bids` / `asks` - 五檔委買委賣

### 當日 K 線（分鐘）
```bash
curl -s "https://api.fugle.tw/marketdata/v1.0/stock/intraday/candles/{股票代碼}" \
  -H "X-API-KEY: $FUGLE_API_KEY" | python3 -m json.tool
```

### 歷史日 K
```bash
curl -s "https://api.fugle.tw/marketdata/v1.0/stock/historical/candles/{股票代碼}?from=2026-01-01&to=2026-02-23" \
  -H "X-API-KEY: $FUGLE_API_KEY" | python3 -m json.tool
```

### 個股基本資訊
```bash
curl -s "https://api.fugle.tw/marketdata/v1.0/stock/intraday/ticker/{股票代碼}" \
  -H "X-API-KEY: $FUGLE_API_KEY" | python3 -m json.tool
```

### 大盤加權指數
```bash
curl -s "https://api.fugle.tw/marketdata/v1.0/stock/intraday/quote/IX0001" \
  -H "X-API-KEY: $FUGLE_API_KEY" | python3 -m json.tool
```

## 方法 2：Shioaji 備援

當 Fugle API 失敗時使用。需要 Python 環境。

```python
import shioaji as sj
import os

api = sj.Shioaji()
api.login(
    api_key=os.getenv('SINOTRADE_API_KEY'),
    secret_key=os.getenv('SINOTRADE_SECRET_KEY')
)

# 查詢台積電
contract = api.Contracts.Stocks["2330"]
snapshot = api.snapshots([contract])
print(snapshot)

api.logout()
```

### 快速 one-liner
```bash
source ~/.zshrc && python3 -c "
import shioaji as sj, os
api = sj.Shioaji()
api.login(api_key=os.getenv('SINOTRADE_API_KEY'), secret_key=os.getenv('SINOTRADE_SECRET_KEY'))
contract = api.Contracts.Stocks['2308']
snap = api.snapshots([contract])[0]
print(f'{contract.name} 現價:{snap.close} 漲跌:{snap.change_price} ({snap.change_rate}%)')
api.logout()
"
```

## 方法 3：Yahoo Finance 備援

不需要 API Key，完全免費。台股代碼加 `.TW`，上櫃加 `.TWO`。

### 即時報價
```bash
curl -s "https://query1.finance.yahoo.com/v8/finance/chart/2308.TW?interval=1d&range=1d" \
  | python3 -c "
import sys,json
d=json.load(sys.stdin)['chart']['result'][0]
meta=d['meta']
print(f\"{meta['symbol']} 現價:{meta['regularMarketPrice']} 昨收:{meta['previousClose']}\")
print(f\"漲跌:{meta['regularMarketPrice']-meta['previousClose']:.2f}\")
"
```

### 歷史數據
```bash
# 近 3 個月日 K
curl -s "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?interval=1d&range=3mo" | python3 -m json.tool
```

### 常用參數
- `interval`: 1m, 5m, 15m, 1d, 1wk, 1mo
- `range`: 1d, 5d, 1mo, 3mo, 6mo, 1y, 5y, max

### 注意
- 台股代碼格式：`2330.TW`（上市）、`6547.TWO`（上櫃）
- 不需認證，但有 rate limit
- 數據可能延遲 15-20 分鐘

## 查價流程

1. **先用 Fugle** → `curl` 一行搞定，即時數據
2. **Fugle 失敗** → 改用 Yahoo Finance（免費免 key）
3. **Yahoo 也失敗** → 改用 Shioaji（需 Python）
4. **都失敗** → 用 web_search 搜即時股價

## 輸出格式建議

```
📈 台達電 (2308)
• 現價：$1,365
• 開盤：$1,320
• 最高：$1,380 / 最低：$1,295
• 昨收：$1,260
• 漲跌：+$105（+8.33%）🔥
```

## 批次查詢多檔

```bash
source ~/.zshrc
for code in 2330 2308 2317 2454; do
  echo "=== $code ==="
  curl -s "https://api.fugle.tw/marketdata/v1.0/stock/intraday/quote/$code" \
    -H "X-API-KEY: $FUGLE_API_KEY" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(f\"{d['name']} 現價:{d['lastPrice']} 漲跌:{d['change']}({d['changePercent']}%)\")
"
done
```

## 注意事項
- Fugle API 交易時間（09:00-13:30）回傳即時數據，盤後回傳收盤數據
- Shioaji 需要先 `pip install shioaji`（已裝在 stock-analyzer venv）
- API Key 都在 `~/.zshrc` 環境變數中
- Fugle 文件：https://developer.fugle.tw/docs/

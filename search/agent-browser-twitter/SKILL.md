---
name: agent-browser-twitter
description: 用 agent-browser + agentcore profile 搜尋 Twitter/X。當需要搜尋推文、查看用戶、瀏覽 Twitter 時使用。取代 bird CLI，不會被擋。
---

# Agent Browser Twitter

用 `agent-browser -p agentcore` 操作 Twitter/X，已注入 cookie 登入。

## ⚡ 快速開啟（推薦）

使用 wrapper script 自動處理 cookie 注入：

```bash
# 搜尋推文（自動注入 cookie + 檢查登入）
bash ~/.openclaw/scripts/twitter-browser.sh "https://x.com/search?q=關鍵字&f=live"
agent-browser snapshot

# 檢查登入狀態
bash ~/.openclaw/scripts/twitter-browser.sh --check-only
```

## 搜尋推文

```bash
# 搜尋關鍵字（最新）
bash ~/.openclaw/scripts/twitter-browser.sh "https://x.com/search?q=關鍵字&f=live"
agent-browser snapshot

# 搜尋關鍵字（熱門）
bash ~/.openclaw/scripts/twitter-browser.sh "https://x.com/search?q=關鍵字&f=top"
agent-browser snapshot
```

## 查看用戶 / 特定推文

```bash
bash ~/.openclaw/scripts/twitter-browser.sh "https://x.com/用戶名"
bash ~/.openclaw/scripts/twitter-browser.sh "https://x.com/用戶名/status/推文ID"
agent-browser snapshot
```

## 操作頁面

```bash
agent-browser click @e5           # 點擊
agent-browser scroll down 500     # 滾動
agent-browser snapshot            # 重新取得結構
agent-browser screenshot ~/path/to/output.png  # 截圖
```

## Cookie 完全失效時

如果 wrapper script 報 ERROR，需要更新 credentials：

1. 用瀏覽器登入 x.com
2. 從 DevTools > Application > Cookies 取得新的 `auth_token` 和 `ct0`
3. 更新 `~/.config/bird/credentials.json`

## 🤖 反偵測：自然互動行為

搜尋瀏覽推文時，**像真人一樣互動**，降低被 Twitter 擋的風險：

1. **按讚（Like）** — 看到跟搜尋主題相關的好推文，點 Like 按鈕（ref 通常是 "X Likes. Like"）
2. **收藏（Bookmark）** — 看到值得參考的推文，點 Bookmark 按鈕
3. **不要每篇都按** — 隨機選 1-3 篇互動就好，太規律反而可疑
4. **上下滾動** — 像真人一樣來回瀏覽，不要只往下衝

```bash
# 範例：對某篇推文按讚
agent-browser click @e66    # "X Likes. Like" 按鈕

# 範例：收藏某篇推文
agent-browser click @e68    # "Bookmark" 按鈕

# 範例：自然滾動（隨機距離，像人在來回看）
# 每次用不同的數字！不要固定，用 $((RANDOM % 300 + 200)) 產生隨機值
agent-browser scroll down $((RANDOM % 400 + 200))
agent-browser scroll up $((RANDOM % 200 + 50))
agent-browser scroll down $((RANDOM % 300 + 150))
```

**原則：**
- 搜尋時順手互動 1-3 篇，不要刻意，像人一樣自然瀏覽
- **不要頻繁 open 新 URL！** 換關鍵字時用搜尋框（清空 → 輸入新關鍵字 → Enter），不要每次都 `agent-browser open` 新網址
- 在同一頁慢慢瀏覽，不要快速跳頁

```bash
# ✅ 正確：用搜尋框換關鍵字
agent-browser fill @搜尋框ref "新關鍵字"
agent-browser press Enter

# ❌ 錯誤：每次都開新 URL
agent-browser open "https://x.com/search?q=新關鍵字"
```

## 注意事項

- **永遠用 wrapper script 開啟** — 自動處理 cookie 注入和過期問題
- 用完記得 `agent-browser close` 釋放資源
- Credentials 位置：`~/.config/bird/credentials.json`

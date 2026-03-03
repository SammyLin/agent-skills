---
name: cloudflare
description: Cloudflare 操作工具。當需要管理 Cloudflare Tunnel、R2 CDN、DNS、Pages 部署時使用。包括啟動 tunnel、上傳檔案、部署網站等常見操作。Do not use for: AWS/GCP/Azure 部署、Vercel/Netlify 部署、域名購買、SSL 憑證管理（Cloudflare 自動處理）、或應用程式開發本身。
---

# Cloudflare 操作

## Cloudflare Tunnel

### 啟動 Tunnel
```bash
cloudflared tunnel --config ~/.cloudflared/config.yml run &
```

### Tunnel 資訊
- **Config 路徑**: `~/.cloudflared/config.yml`
- **Tunnel ID**: 見 `~/.cloudflared/config.yml`
- **文件**: `docs/CLOUDFLARE_TUNNEL_SETUP.md`

### 快速啟動（對外開放）
```bash
cloudflared tunnel --url http://localhost:PORT
```
會產生 `https://xxx.trycloudflare.com` 連結

**優點**：
- 無警告頁面
- 無連線限制
- 速度較快
- 比 ngrok 穩定

---

## R2 CDN（圖床）

### 基本資訊
- **Bucket**: `cdn-3mi`
- **域名**: `https://cdn.3mi.tw`
- **Account/Zone ID**: 見 `~/.cloudflared/credentials.json` 或用 `wrangler whoami` 查詢

### 上傳指令
```bash
npx wrangler r2 object put cdn-3mi/路徑/檔名 --file 本地檔案 --remote
```

### 常用範例
```bash
# 上傳圖片
npx wrangler r2 object put cdn-3mi/blog/image.jpg --file ./image.jpg --remote

# 上傳並指定 content-type
npx wrangler r2 object put cdn-3mi/blog/photo.png --file ./photo.png --remote --content-type image/png
```

### 注意事項
- **必須用 `--remote`**：否則只存 local
- **需要 OAuth 登入**：用 PTY 模式（`pty: true`）
- **帳號區分**：Otto / Sammylintw，3mi.tw 在 Sammylintw 下

---

## Cloudflare Pages

### 部署指令
```bash
# 安裝 wrangler
npm install -g wrangler

# 登入
wrangler login

# 部署
wrangler pages deploy dist --project-name=專案名
```

### 常用範例
```bash
# 部署靜態網站
wrangler pages deploy ./build --project-name=bg-removal

# 綁定自訂網域
wrangler pages domain add bg-removal.3mi.tw
```

---

## DNS 管理

### 常用指令
```bash
# 列出 DNS 記錄
wrangler dns records list --zone-id=ZONE_ID

# 新增 DNS 記錄
wrangler dns records add ZONE_ID A example.com 1.2.3.4
wrangler dns records add ZONE_ID CNAME www example.com
```

---

## 遷移進度

| 網站 | 原部署 | 新部署 | 狀態 |
|------|--------|--------|------|
| bg-removal.3mi.tw | Docker :80 | Cloudflare Pages | ✅ 完成 |
| retrolyze.3mi.tw | Docker :8000 | - | 待遷移 |
| mbti.3mi.tw | Docker :8080 | - | 待遷移 |

---

## 快速參考

| 任務 | 指令 |
|------|------|
| 啟動 tunnel | `cloudflared tunnel --config ~/.cloudflared/config.yml run &` |
| 臨時對外開放 | `cloudflared tunnel --url http://localhost:3000` |
| R2 上傳 | `npx wrangler r2 object put cdn-3mi/path --file file --remote` |
| Pages 部署 | `wrangler pages deploy dist --project-name=xxx` |

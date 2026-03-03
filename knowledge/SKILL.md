---
name: obsidian-workflow
description: Obsidian 筆記操作流程。當需要與 Obsidian vault 同步、讀取、寫入筆記時使用。我們的 vault 在 iCloud（Mochi-Memory），常用於記憶同步、知識庫存取。
---

# Obsidian Workflow

## 我們的 Vault

- **路徑**：`~/Library/Mobile Documents/com~apple~CloudDocs/Mochi-Memory/`
- **同步**：iCloud 自動同步
- **用途**：長期記憶、知識庫、對話風格紀錄

## 常用檔案

| 檔案 | 用途 |
|------|------|
| `MEMORY.md` | Mochi 長期記憶 |
| `memory/YYYY-MM-DD.md` | 每日對話日誌 |
| `32-01 對話風格與工作方式.md` | Sammy 的偏好 |
| `00-09 系統/00 Johnny Decimal 索引.md` | 知識庫索引 |

## 常用指令

### 讀取筆記
```bash
# 讀取特定筆記
cat ~/Library/Mobile\ Documents/com~apple~CloudDocs/Mochi-Memory/MEMORY.md

# 讀取今日記憶
cat ~/Library/Mobile\ Documents/com~apple~CloudDocs/Mochi-Memory/memory/$(date +%Y-%m-%d).md
```

### 搜尋筆記
```bash
# 搜尋關鍵字
grep -r "關鍵字" ~/Library/Mobile\ Documents/com~apple~CloudDocs/Mochi-Memory/

# 找特定日期的記憶
ls ~/Library/Mobile\ Documents/com~apple~CloudDocs/Mochi-Memory/memory/
```

### 寫入筆記
```bash
# 寫入記憶
echo "內容" >> ~/Library/Mobile\ Documents/com~apple~CloudDocs/Mochi-Memory/memory/$(date +%Y-%m-%d).md
```

## 同步腳本

### 同步到 Obsidian
```bash
bash ~/.openclaw/scripts/sync-to-obsidian.sh
```

### 備份記憶
```bash
bash ~/.openclaw/scripts/backup-memory.sh
```

## 應用場景

| 場景 | 動作 |
|------|------|
| 查過往對話 | 搜 memory/ |
| 查 Sammy 偏好 | 讀 32-01 對話風格與工作方式.md |
| 查知識索引 | 讀 00 Johnny Decimal 索引.md |
| 記錄新東西 | 寫入 memory/YYYY-MM-DD.md |

## 與 OpenClaw 記憶的區別

| 系統 | 位置 | 用途 |
|------|------|------|
| **Obsidian** | iCloud | 長期知識庫、可讀取 |
| **OpenClaw memory** | ~/.openclaw/memory/ | 對話記錄、狀態追蹤 |
| **HEARTBEAT.md** | workspace | 定期任務定義 |

## 小技巧

- 用 `memory_search` tool 可以更方便搜尋
- Obsidian 筆記會自動同步到所有設備
- 重要資訊存 Obsidian，對話細節存 OpenClaw memory

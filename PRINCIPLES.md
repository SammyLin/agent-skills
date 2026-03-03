# Micro-Skill Principles

## 1. Micro-Skill 架構
- 就像 Micro-Service 一樣
- 小小的、獨立的、可重複呼叫的元件
- 不要重複寫相同功能 → 用呼叫取代

## 2. 機敏資訊隔離
- 敏感資料不放 SKILL.md
- 用環境變數或外部設定檔

## 3. 優先自建，審慎引用
- 優先用自己的 skill
- 外部 skill 只用於非核心功能

## 4. 精準描述（Skill Description）
- 清楚說什麼時候**要用**
- 清楚說什麼時候**不要用**
- 包含關鍵字，AI 容易 match
- 範例：`"用於：查詢台股即時報價。不要用於：虛擬貨幣、美股。"`

## 5. Progressive Disclosure
- 先載入 metadata (name, description)
- 實際用到才載入完整 SKILL.md
- 省 token，提效能

## 6. Skill 結構
```
skill-name/
├── SKILL.md      # 必要：名稱 + 描述 + 指令
├── scripts/      # 選用：可執行腳本
├── references/   # 選用：文件參考
└── assets/       # 選用：模板、資源
```

## 7. Skill Usage Tracking
- 每次使用 skill 時記錄下來
- 每 2 天 review 使用次數
- 沒用到的 skill 考慮刪除或合併

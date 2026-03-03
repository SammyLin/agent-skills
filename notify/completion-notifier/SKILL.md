---
name: completion-notifier
description: 任務完成通知格式。當完成任務後需要發送通知給使用者時使用，包括：代碼完成、資料蒐集結束、任務結束等場景。自動格式化輸出，包含任務名稱、檔案位置、Linear 連結、摘要。Do not use for: 任務執行本身、錯誤通知、進度中的狀態更新、或與使用者的一般對話。
---

# Completion Notifier

## 通知格式

完成任務後，自動發送以下格式：

```
✅ [任務名稱] 完成！
📍 檔案：xxx
📋 Linear：[OTT-XX](連結)
💡 摘要：一句話說明做了什麼
```

## 範例

### 範例 1：FB 文章
```
✅ FB 文章完成！
📍 檔案：~/otta.workspace/openclaw-fb-article-v3.txt
📋 Linear：[OTT-39](https://linear.app/sammylin/issue/OTT-39)
💡 簡潔版 9 個重點，適合 FB 貼文
```

### 範例 2：程式開發
```
✅ PPT Translator 整合完成！
📍 檔案：~/otta.workspace/ppt_translator/
📋 Linear：[OTT-45](https://linear.app/sammylin/issue/OTT-45)
💡 新增 WebSocket 即時同步功能
```

### 範例 3：研究任務
```
✅ 研究報告完成！
📍 檔案：~/otta.workspace/research/esp32-buy.md
📋 Linear：[OTT-50](https://linear.app/sammylin/issue/OTT-50)
💡 整理了 Elecrow/Tindie/Amazon 三個購買渠道的價格比較
```

## 發送方式

- **Telegram**: 使用 message tool
- **一般情況**: 直接回覆訊息
- **複雜輸出**: 加上適當分隔線

## 注意事項

- 檔案路徑用 `~/` 表示 home 目錄
- Linear 連結用完整 URL
- 摘要一句話就好，不要太長
- 如果沒有檔案，可以省略「📍 檔案：」

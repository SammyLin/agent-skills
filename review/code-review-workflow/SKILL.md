---
name: code-review-workflow
description: Code review 流程。當需要檢視 PR、處理 review comments、合併分支時使用。基於 GitHub gh CLI 操作，包括檢查 PR 狀態、查看 CI 結果、處理 review 意見、決定是否合併。Do not use for: 寫新代碼、建立 PR（用 git commit + gh pr create）、Linear issue 管理、或非 GitHub 平台的 code review。
---

# Code Review Workflow

## 基礎指令

### 查看 PR 列表
```bash
gh pr list --state all
gh pr list --state open
```

### 查看 PR 詳情
```bash
gh pr view 123
gh pr view 123 --json title,body,state,mergeable
```

### 查看 PR diff
```bash
gh pr diff 123
gh pr diff 123 --stat  # 僅統計
```

### 查看 CI 狀態
```bash
gh run list --branch feature-xxx
gh run view <run-id>
```

## Review 流程

### 1. 收到 Review Request
```bash
gh pr view <number>
# 檢視標題、描述、變更
```

### 2. 檢查 CI
```bash
gh run list --branch <branch-name>
# 確認 all checks passed
```

### 3. 閱讀 Code
```bash
gh pr diff <number> | head -100
# 查看變更內容
```

### 4. 給 Review Comment
```bash
gh pr comment <number> --body "意見內容"
```

### 5. 批准或 Request Changes
```bash
gh pr review <number> --approve
gh pr review <number> --request-changes --body "需要修改"
```

## Merge 決策

### 合併條件
- ✅ CI 全部通過
- ✅ 至少 1 人 approve
- ✅ 沒有 blocking comments

### 合併指令
```bash
gh pr merge <number> --squash --delete-branch
```

### 保持分支更新
```bash
git fetch origin
git merge origin/main
```

## 常見狀況

| 狀況 | 處理方式 |
|------|----------|
| CI 失敗 | 不要合併，先問作者 |
| 只有 1 approve | 可以合併 |
| 有 request changes | 需要作者修改後重新 review |
| conflict | 要求作者 rebase |

## 使用 gh-issues Skill

如果需要連動 Linear issue：
- 在 PR description 標記 Linear issue
- 完成後在 issue comment 記錄 PR 連結

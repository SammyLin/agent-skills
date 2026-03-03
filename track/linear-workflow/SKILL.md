---
name: linear-workflow
description: Linear issue 管理流程。當需要建立、更新或追蹤 Linear issue 時使用，包括：建立新 issue、添加 comment、更新狀態、追蹤任務進度。適用於任何任務管理、工作分配、進度追蹤的場景。Do not use for: 產品規劃討論（用 product-planning）、GitHub Issues、Linear CLI 指令參考（用 linear-cli）、或非任務管理的一般查詢。
---

# Linear Workflow

> CLI 指令語法請參考 `linear-cli` skill，本 skill 專注於團隊規則、GraphQL API 用法與連結格式。

## 團隊使用規則

**OTT Team** - 我們（Sammy + Mochi）的事項
- 連結：https://linear.app/sammylin/team/OTT/all
- 用途：所有跟 Mochi 的對話、任務、專案

**DECT Team** - Sammy 的工作（Delta 相關）
- 連結：https://linear.app/sammylin/team/DECT
- 用途：只有 Sammy 的個人工作

## GraphQL API（當 CLI 不適用時）

認證方式：
```bash
-H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)"
```

常用 mutation/query 範例見 [references/graphql-examples.md](references/graphql-examples.md)。

## 連結格式

顯示卡片時用 markdown 連結：
```
[DECT-XXX](https://linear.app/sammylin/issue/DECT-XXX)
[OTT-XXX](https://linear.app/sammylin/issue/OTT-XXX)
```

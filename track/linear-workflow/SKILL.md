---
name: linear-workflow
description: Linear issue 管理流程。當需要建立、更新或追蹤 Linear issue 時使用，包括：建立新 issue、添加 comment、更新狀態、追蹤任務進度。適用於任何任務管理、工作分配、進度追蹤的場景。
---

# Linear Workflow

## 團隊使用規則

**OTT Team** - 我們（Sammy + Mochi）的事項
- 連結：https://linear.app/sammylin/team/OTT/all
- 用途：所有跟 Mochi 的對話、任務、專案

**DECT Team** - Sammy 的工作（Delta 相關）
- 連結：https://linear.app/sammylin/team/DECT
- 用途：只有 Sammy 的個人工作

## 建立 Issue

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { issueCreate(input: { teamId: \"TEAM_ID\", title: \"標題\", description: \"描述\" }) { success issue { id title } } }"
  }'
```

取得 Team ID：
```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { teams { nodes { id name key } } }"}'
```

- OTT: `532cea28-6b09-438e-8cd1-6b3e09a50cec`
- DECT: `96e2e3cf-9cc4-493c-b412-aca151bd843a`

## 更新 Issue

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { issueUpdate(id: \"ISSUE_ID\", input: { stateId: \"STATE_ID\" }) { success } }"
  }'
```

## 新增 Comment

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { commentCreate(input: { issueId: \"ISSUE_ID\", body: \"內容\" }) { success } }"
  }'
```

## 查詢 Issue

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { issue(id: \"ISSUE_ID\") { id title description state { name } assignee { name } } }"}'
```

## 查詢團隊 Issues

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { team(id: \"TEAM_ID\") { issues(first: 10, filter: { state: { name: { eq: \"Backlog\" } } }) { nodes { id title state { name } } } } }"
  }'
```

## 連結格式

顯示卡片時用 markdown 連結：
```
[DECT-XXX](https://linear.app/sammylin/issue/DECT-XXX)
[OTT-XXX](https://linear.app/sammylin/issue/OTT-XXX)
```

# Linear GraphQL API Examples

所有請求都發到 `https://api.linear.app/graphql`，認證方式：
```bash
-H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)"
-H "Content-Type: application/json"
```

## 取得 Team ID

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { teams { nodes { id name key } } }"}'
```

## 建立 Issue

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Authorization: $(cat ~/.linear | grep api_key | cut -d'=' -f2)" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { issueCreate(input: { teamId: \"TEAM_ID\", title: \"標題\", description: \"描述\" }) { success issue { id title } } }"
  }'
```

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

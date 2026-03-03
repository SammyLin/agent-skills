# n8n Configuration Patterns

Detailed reference for property dependencies, node configuration patterns, and operation-specific examples.

## Property Dependencies Deep Dive

### displayOptions Mechanism

**Fields have visibility rules**:

```javascript
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true],
      "method": ["POST", "PUT", "PATCH"]
    }
  }
}
```

**Translation**: "body" field shows when:
- sendBody = true AND
- method = POST, PUT, or PATCH

### Common Dependency Patterns

#### Pattern 1: Boolean Toggle

**Example**: HTTP Request sendBody
```javascript
{
  "sendBody": true   // body field appears
}
```

#### Pattern 2: Operation Switch

**Example**: Slack resource/operation
```javascript
// Different operations -> different fields
{
  "resource": "message",
  "operation": "post"
  // Shows: channel, text, attachments, etc.
}

{
  "resource": "message",
  "operation": "update"
  // Shows: messageId, text (different fields!)
}
```

#### Pattern 3: Type Selection

**Example**: IF node conditions
```javascript
{
  "type": "string",
  "operation": "contains"
  // Shows: value1, value2
}

{
  "type": "boolean",
  "operation": "equals"
  // Shows: value1, value2, different operators
}
```

### Using get_property_dependencies

```javascript
const deps = get_property_dependencies({
  nodeType: "nodes-base.httpRequest"
});

// Returns dependency tree
{
  "dependencies": {
    "body": {
      "shows_when": {
        "sendBody": [true],
        "method": ["POST", "PUT", "PATCH", "DELETE"]
      }
    },
    "queryParameters": {
      "shows_when": {
        "sendQuery": [true]
      }
    }
  }
}
```

## Common Node Patterns

### Pattern 1: Resource/Operation Nodes

**Examples**: Slack, Google Sheets, Airtable

```javascript
{
  "resource": "<entity>",      // What type of thing
  "operation": "<action>",     // What to do with it
  // ... operation-specific fields
}
```

**How to configure**:
1. Choose resource
2. Choose operation
3. Use get_node_essentials to see operation-specific requirements
4. Configure required fields

### Pattern 2: HTTP-Based Nodes

**Examples**: HTTP Request, Webhook

```javascript
{
  "method": "<HTTP_METHOD>",
  "url": "<endpoint>",
  "authentication": "<type>",
  // ... method-specific fields
}
```

**Dependencies**:
- POST/PUT/PATCH -> sendBody available
- sendBody=true -> body required
- authentication != "none" -> credentials required

### Pattern 3: Database Nodes

**Examples**: Postgres, MySQL, MongoDB

```javascript
{
  "operation": "<query|insert|update|delete>",
  // ... operation-specific fields
}
```

**Dependencies**:
- operation="executeQuery" -> query required
- operation="insert" -> table + values required
- operation="update" -> table + values + where required

### Pattern 4: Conditional Logic Nodes

**Examples**: IF, Switch, Merge

```javascript
{
  "conditions": {
    "<type>": [
      {
        "operation": "<operator>",
        "value1": "...",
        "value2": "..."  // Only for binary operators
      }
    ]
  }
}
```

**Dependencies**:
- Binary operators (equals, contains, etc.) -> value1 + value2
- Unary operators (isEmpty, isNotEmpty) -> value1 only + singleValue: true

## Operation-Specific Configuration

### Slack Node Examples

#### Post Message
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",      // Required
  "text": "Hello!",           // Required
  "attachments": [],          // Optional
  "blocks": []                // Optional
}
```

#### Update Message
```javascript
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890",  // Required (different from post!)
  "text": "Updated!",         // Required
  "channel": "#general"       // Optional (can be inferred)
}
```

#### Create Channel
```javascript
{
  "resource": "channel",
  "operation": "create",
  "name": "new-channel",      // Required
  "isPrivate": false          // Optional
}
```

### HTTP Request Node Examples

#### GET Request
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth",
  "sendQuery": true,
  "queryParameters": {
    "parameters": [
      { "name": "limit", "value": "100" }
    ]
  }
}
```

#### POST with JSON
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

### IF Node Examples

#### String Comparison (Binary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"              // Binary: needs value2
      }
    ]
  }
}
```

#### Empty Check (Unary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.email}}",
        "operation": "isEmpty",
        "singleValue": true             // Auto-added by sanitization
      }
    ]
  }
}
```

## Handling Conditional Requirements

### HTTP Request Body

**Rule**:
```
body is required when:
  - sendBody = true AND
  - method IN (POST, PUT, PATCH, DELETE)
```

**How to discover**:
```javascript
// Option 1: Read validation error
validate_node_operation({...});

// Option 2: Check dependencies
get_property_dependencies({
  nodeType: "nodes-base.httpRequest"
});

// Option 3: Try minimal config and iterate
```

### IF Node singleValue

**Rule**:
```
singleValue should be true when:
  - operation IN (isEmpty, isNotEmpty, true, false)
```

**Good news**: Auto-sanitization fixes this!

## Configuration Anti-Patterns

### Don't: Over-configure Upfront

**Bad**:
```javascript
{
  "method": "GET",
  "url": "...",
  "sendQuery": false,
  "sendHeaders": false,
  "sendBody": false,
  "timeout": 10000,
  "ignoreResponseCode": false,
  // ... 20 more optional fields
}
```

**Good**:
```javascript
{
  "method": "GET",
  "url": "...",
  "authentication": "none"
}
```

### Don't: Skip Validation

**Bad**:
```javascript
const config = {...};
n8n_update_partial_workflow({...});  // YOLO
```

**Good**:
```javascript
const config = {...};
const result = validate_node_operation({...});
if (result.valid) {
  n8n_update_partial_workflow({...});
}
```

### Don't: Ignore Operation Context

**Bad**:
```javascript
// Same config for all Slack operations, then switching operation without updating
{
  "resource": "message",
  "operation": "update",  // Changed
  "channel": "#general",  // Wrong field for update!
  "text": "..."
}
```

**Good**:
```javascript
// Check requirements when changing operation
get_node_essentials({
  nodeType: "nodes-base.slack"
});
```

## Best Practices

### Do

1. **Start with get_node_essentials** - 91.7% success rate, faster than get_node_info
2. **Validate iteratively** - Configure -> Validate -> Fix -> Repeat (2-3 iterations normal)
3. **Use property dependencies when stuck** - Understand field visibility rules
4. **Respect operation context** - Different operations = different requirements
5. **Trust auto-sanitization** - Operator structure fixed automatically

### Don't

1. **Jump to get_node_info immediately** - Try essentials first
2. **Configure blindly** - Always validate before deploying
3. **Copy configs without understanding** - Validate after copying
4. **Manually fix auto-sanitization issues** - Let system handle operator structure

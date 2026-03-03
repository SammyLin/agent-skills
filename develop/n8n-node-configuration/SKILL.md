---
name: n8n-node-configuration
description: Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node_essentials and get_node_info, or learning common configuration patterns by node type. Do not use for: n8n installation/setup, workflow design from scratch, non-n8n automation platforms (Zapier, Make), or general API integration without n8n.
---

# n8n Node Configuration

Expert guidance for operation-aware node configuration with property dependencies.

## Configuration Philosophy

**Progressive disclosure**: Start minimal, add complexity as needed.

- get_node_essentials is the most used discovery pattern (91.7% success rate)
- Most configurations need only essentials, not full schema

## Core Concepts

### 1. Operation-Aware Configuration

**Not all fields are always required** - it depends on operation!

Resource + operation determine which fields are required. Example: Slack "post" needs channel+text, but "update" needs messageId+text.

### 2. Property Dependencies

Fields appear/disappear based on other field values via displayOptions. Example: HTTP Request "body" only shows when sendBody=true AND method is POST/PUT/PATCH.

### 3. Progressive Discovery

1. **get_node_essentials** (use first - 91.7% success rate): Quick overview, required fields, common options
2. **get_property_dependencies** (for complex nodes): Shows conditional requirements
3. **get_node_info** (full schema): Complete documentation, all fields

## Configuration Workflow

```
1. Identify node type and operation
2. Use get_node_essentials
3. Configure required fields
4. Validate configuration
5. If dependencies unclear -> get_property_dependencies
6. Add optional fields as needed
7. Validate again
8. Deploy
```

## get_node_essentials vs get_node_info

Use **get_node_essentials** when starting configuration (~18 seconds average). Returns required fields, common options, basic examples, operation list.

Use **get_node_info** when essentials are insufficient. Returns full schema, all properties, advanced options. Slower but complete.

```
Starting new config? -> get_node_essentials
  Sufficient? -> Configure with essentials
  Need dependency info? -> get_property_dependencies
  Still need more? -> get_node_info
```

## Summary

**Configuration Strategy**:
1. Start with get_node_essentials (91.7% success)
2. Configure required fields for operation
3. Validate configuration
4. Check dependencies if stuck
5. Iterate until valid (avg 2-3 cycles)
6. Deploy with confidence

**Key Principles**:
- **Operation-aware**: Different operations = different requirements
- **Progressive disclosure**: Start minimal, add as needed
- **Dependency-aware**: Understand field visibility rules
- **Validation-driven**: Let validation guide configuration

## Detailed References

- **[references/configuration-patterns.md](references/configuration-patterns.md)** - Property dependencies deep dive, node patterns, operation-specific examples, anti-patterns, and best practices
- **[references/DEPENDENCIES.md](references/DEPENDENCIES.md)** - Deep dive into property dependencies and displayOptions
- **[references/OPERATION_PATTERNS.md](references/OPERATION_PATTERNS.md)** - Common configuration patterns by node type

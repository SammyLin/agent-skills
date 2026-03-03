---
name: image-gen-workflow
description: AI 圖片生成與發送流程。當需要生成圖片並發送給使用者時使用。支援 nano-banana-pro（Gemini）和 OpenAI 兩種圖片生成服務，生成後自動發送到 Telegram。
---

# Image Gen Workflow

## 工具選擇

### nano-banana-pro（推薦）
- 模型：Gemini 2.0 Pro Image
- 指令：使用 nano-banana-pro skill
- 優點：免費、效果好

### openai-image-gen
- 模型：DALL-E 3
- 指令：使用 openai-image-gen skill
- 優點：穩定、速度快

## 生成流程

### 1. 生成圖片
```bash
# 使用 nano-banana-pro
# 讀取 skill 了解用法
read ~/.openclaw/skills/nano-banana-pro/SKILL.md

# 或使用 openai-image-gen
read ~/.openclaw/skills/openai-image-gen/SKILL.md
```

### 2. 發送圖片
生成後，使用 message tool 發送到 Telegram：

```bash
message action=send to=163411431 media=/path/to/image.jpg caption="圖片描述"
```

## 發送格式

### Telegram
- 直接發送圖片 + 簡短說明
- caption 最多 1024 字元

### 範例
```
🌟 圖片生成完成！
[圖片]

這是根據你的描述生成的～
```

## 圖片優化技巧

### prompt 建議
- 具體描述場景、氛圍
- 指定風格（寫實、卡通、極簡等）
- 加入光線、構圖指示

### 範例
```
Prompt: A cute mochi character with big eyes, holding a small flag, soft pastel colors, kawaii style, transparent background, minimal design
```

## 注意事項

- 生成後**立刻發送**，不要等使用者問
- 發送時加上簡短說明
- 如果需要多張，一次生成全部再發送

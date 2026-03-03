---
name: mlx-whisper
description: MLX Whisper 本地語音轉文字。用於將音訊檔案轉換為文字（Speech-to-Text），完全在本地執行（Apple Silicon），免費且隱私。當需要離線語音轉文字、不想花 API 費用、或需要快速轉換時使用。
---

# MLX Whisper

MLX Whisper 是 Apple Silicon 優化的 Whisper 實作，完全本地執行，免費快速。

## 安裝

```bash
pip install lightning-whisper-mlx
```

需要：
- Python 3.9+
- Apple Silicon Mac（M1/M2/M3/M4）
- macOS 12.3+

## 基本用法

### 命令列

```bash
# 安裝後使用 whisper 命令
whisper audio.mp3 --model base

# 指定模型大小
whisper audio.mp3 --model small   # ~75MB
whisper audio.mp3 --model medium  # ~769MB
whisper audio.mp3 --model large   # ~1550MB

# 指定語言（可加速）
whisper audio.mp3 --language zh   # 中文
whisper audio.mp3 --language en   # 英文

# 輸出格式
whisper audio.mp3 --output_format txt
whisper audio.mp3 --output_format srt
whisper audio.mp3 --output_format vtt
```

### Python API

```python
from lightning_whisper_mlx import LightningWhisperMLX

model = LightningWhisperMLX(model="base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## 可用模型

| 模型 | 大小 | 速度 |
|------|------|------|
| tiny | ~75MB | 最快 |
| base | ~75MB | 快 |
| small | ~244MB | 中 |
| medium | ~769MB | 慢 |
| large | ~1550MB | 最慢 |

## 與其他 Whisper 的選擇

| Skill | 適用場景 |
|-------|----------|
| **mlx-whisper** | 本地、免費、隱私（Apple Silicon） |
| **groq-whisper** | 線上、快速、免費額度（Groq API） |
| **openai-whisper-api** | 線上、穩定、付費（OpenAI API） |
| **openai-whisper** | 本地、通用（PyTorch） |

## 輸出格式

轉換後可以输出：
- `.txt` - 純文字
- `.srt` - 字幕格式
- `.vtt` - WebVTT 字幕
- `.json` - 詳細輸出（含時間戳）

## 技巧

- 首次使用會下載模型，之後會快很多
- 小音量或背景噪音會影響準確率
- 可以先用 `base` 模型測試，再根據需求選擇更大的模型

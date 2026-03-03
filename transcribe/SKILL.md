---
name: whisper
description: "Audio transcription. Use for: converting audio to text. Do not use for: video transcription, translation."
---

# Whisper - Unified Audio Transcription

Unified interface for audio transcription. Delegates to specific providers based on context.

## Providers

### Groq Whisper (Online)
- Fast, uses Groq API
- Best for: quick transcription, multiple files
- When: user wants speed

### MLX Whisper (Local)
- Runs locally on Apple Silicon
- Best for: privacy-sensitive content, offline
- When: user wants privacy or offline

## Usage

Simply use this skill - it will choose the appropriate provider automatically.

For direct access:
- Groq: Use groq-whisper skill
- MLX: Use mlx-whisper skill

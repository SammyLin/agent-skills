---
name: youtube
description: Extract and summarize YouTube video content. Use when user provides a YouTube URL and wants transcript, summary, key points, or content analysis. Supports auto-generated and manual subtitles in multiple languages. Do not use for: downloading videos, non-YouTube platforms (Vimeo, Bilibili), local audio/video transcription (use mlx-whisper), or video editing.
---

# YouTube Content Extractor

Extract transcripts and summarize YouTube videos using `yt-dlp`.

## Prerequisites

- `yt-dlp` installed (`brew install yt-dlp`)

## Quick Start

### Get transcript (auto-detect language)
```bash
~/.ai/skills/youtube/scripts/yt-transcript.sh "YOUTUBE_URL"
```

### Get transcript with specific language
```bash
~/.ai/skills/youtube/scripts/yt-transcript.sh "YOUTUBE_URL" zh  # 中文
~/.ai/skills/youtube/scripts/yt-transcript.sh "YOUTUBE_URL" en  # English
```

### Get video info only (title, description, duration)
```bash
~/.ai/skills/youtube/scripts/yt-info.sh "YOUTUBE_URL"
```

## Workflow

1. User provides YouTube URL
2. Run `yt-info.sh` to get video metadata
3. Run `yt-transcript.sh` to extract transcript
4. Summarize or analyze the content as requested

## Output Location

Transcripts are saved to `/tmp/youtube/` with the video ID as filename.

## Language Codes

Common codes: `zh` (中文), `en` (English), `ja` (日本語), `ko` (한국어)

## Handling No Subtitles

If no subtitles available:
1. Download audio: `yt-dlp -x --audio-format mp3 -o "/tmp/youtube/%(id)s.%(ext)s" "URL"`
2. Use Whisper or other transcription service

## Tips

- Auto-generated subtitles (`--write-auto-sub`) are available for most videos
- Manual subtitles (`--write-sub`) are higher quality when available
- Use `--sub-lang zh,zh-TW,zh-Hant,en` to try multiple variants

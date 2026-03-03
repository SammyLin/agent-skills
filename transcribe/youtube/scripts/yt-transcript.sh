#!/bin/bash
# Extract YouTube transcript/subtitles
# Usage: yt-transcript.sh "URL" [lang]

set -e

URL="$1"
LANG="${2:-zh,zh-TW,zh-Hant,en,ja,ko}"

if [ -z "$URL" ]; then
    echo "Usage: $0 <youtube-url> [language-code]"
    echo "Example: $0 'https://youtube.com/watch?v=xxx' zh"
    exit 1
fi

# Create output directory
mkdir -p /tmp/youtube

# Extract video ID
VIDEO_ID=$(yt-dlp --print id "$URL" 2>/dev/null)

if [ -z "$VIDEO_ID" ]; then
    echo "Error: Could not extract video ID from URL"
    exit 1
fi

OUTPUT_DIR="/tmp/youtube"
SUB_FILE=""

# Try to get manual subtitles first, then auto-generated
echo "Fetching subtitles for: $VIDEO_ID"
echo "Languages: $LANG"

# Try manual subtitles
yt-dlp --write-sub --sub-lang "$LANG" --skip-download \
    -o "$OUTPUT_DIR/%(id)s" "$URL" 2>/dev/null || true

# If no manual subs, try auto-generated
if ! ls "$OUTPUT_DIR/$VIDEO_ID"*.vtt 2>/dev/null; then
    echo "No manual subtitles, trying auto-generated..."
    yt-dlp --write-auto-sub --sub-lang "$LANG" --skip-download \
        -o "$OUTPUT_DIR/%(id)s" "$URL" 2>/dev/null || true
fi

# Find the subtitle file
SUB_FILE=$(ls "$OUTPUT_DIR/$VIDEO_ID"*.vtt 2>/dev/null | head -1)

if [ -z "$SUB_FILE" ]; then
    echo "Error: No subtitles available for this video"
    echo "You may need to download audio and use Whisper for transcription"
    exit 1
fi

echo "Found: $SUB_FILE"

# Convert VTT to plain text (remove timestamps and formatting)
OUTPUT_TXT="$OUTPUT_DIR/${VIDEO_ID}_transcript.txt"

# Parse VTT: remove WEBVTT header, timestamps, positioning, and empty lines
sed -e '/^WEBVTT/d' \
    -e '/^Kind:/d' \
    -e '/^Language:/d' \
    -e '/^[0-9][0-9]:[0-9][0-9]/d' \
    -e '/^$/d' \
    -e 's/<[^>]*>//g' \
    "$SUB_FILE" | \
    # Remove duplicate consecutive lines (VTT often has overlapping text)
    awk '!seen[$0]++' > "$OUTPUT_TXT"

echo ""
echo "=== Transcript saved to: $OUTPUT_TXT ==="
echo ""
cat "$OUTPUT_TXT"

#!/bin/bash
# Get YouTube video information
# Usage: yt-info.sh "URL"

set -e

URL="$1"

if [ -z "$URL" ]; then
    echo "Usage: $0 <youtube-url>"
    exit 1
fi

echo "=== Video Information ==="
echo ""

# Get video metadata in JSON format
yt-dlp --print "%(title)s" --print "%(channel)s" --print "%(upload_date)s" \
    --print "%(duration_string)s" --print "%(view_count)s" --print "%(description)s" \
    "$URL" 2>/dev/null | {
    read -r title
    read -r channel
    read -r upload_date
    read -r duration
    read -r views
    # Read rest as description
    description=$(cat)
    
    echo "Title: $title"
    echo "Channel: $channel"
    echo "Upload Date: $upload_date"
    echo "Duration: $duration"
    echo "Views: $views"
    echo ""
    echo "=== Description ==="
    echo "$description"
}

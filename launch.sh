#!/usr/bin/env bash
# Mariam Hisham Mohamed AbdelFadil - Grade 8 Into Math Dashboard Launcher
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

PORT=8080
# If 8080 is in use, find an available port
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; do
    PORT=$((PORT+1))
done

echo "=========================================================="
echo "🌟 Launching Mariam's Grade 8 Into Math Dashboard..."
echo "📍 Serving from: $DIR"
echo "🌐 URL: http://localhost:$PORT"
echo "=========================================================="

# Open browser in background
(sleep 1 && open "http://localhost:$PORT") &

# Start python static server
python3 -m http.server $PORT

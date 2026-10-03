#!/bin/bash
# Start local development server

echo "🚀 Starting CodesbyFebin local server..."
echo "📍 Server will be available at http://localhost:8080"
echo ""

# Check if Python is available (preferred for simple HTTP server)
if command -v python3 &> /dev/null; then
    echo "Using Python3 http.server"
    cd "$(dirname "$0")/.."
    python3 -m http.server 8080
elif command -v python &> /dev/null; then
    echo "Using Python http.server"
    cd "$(dirname "$0")/.."
    python -m SimpleHTTPServer 8080
# Check if Node.js http-server is available
elif command -v http-server &> /dev/null; then
    echo "Using Node.js http-server"
    cd "$(dirname "$0")/.."
    http-server . -p 8080 --cache 3600
# Check if Ruby is available
elif command -v ruby &> /dev/null; then
    echo "Using Ruby WEBrick"
    cd "$(dirname "$0")/.."
    ruby -run -ehttpd . -p 8080
# Check if PHP is available
elif command -v php &> /dev/null; then
    echo "Using PHP built-in server"
    cd "$(dirname "$0")/.."
    php -S localhost:8080
else
    echo "❌ No suitable HTTP server found!"
    echo "Please install one of: Python 3, Node.js (http-server), Ruby, or PHP"
    exit 1
fi

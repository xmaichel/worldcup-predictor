#!/bin/bash
# sync.sh — Pull → Add → Commit → Push
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR" || exit 1
echo "📥 Pulling..."
git pull --rebase 2>/dev/null || echo "  (no upstream)"
echo "📦 Staging..."
git add -A
if ! git diff --cached --quiet; then
    COMMIT_MSG="sync $(date '+%Y-%m-%d %H:%M %Z')"
    git commit -m "$COMMIT_MSG"
    echo "✅ Committed: $COMMIT_MSG"
else
    echo "ℹ️  No changes"
fi
echo "📤 Pushing..."
git push 2>/dev/null && echo "✅ Pushed" || echo "  (no remote)"

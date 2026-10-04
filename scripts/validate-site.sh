#!/bin/bash
# Validate site structure and files

echo "🔍 Validating CodesbyFebin site structure..."
echo ""

ERRORS=0

# Check required files
echo "Checking required files..."
REQUIRED_FILES=(
    "index.html"
    "about.html"
    "blog/index.html"
    "projects-enhanced.html"
    "portfolio.html"
    "docs/index.html"
    "docs/research.html"
    "sitemap.xml"
    "robots.txt"
    "llms.txt"
    "vercel.json"
    ".nojekyll"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ Missing: $file"
        ((ERRORS++))
    fi
done

echo ""
echo "Checking documentation files..."
DOC_FILES=(
    "PERFORMANCE_AUDIT.md"
    "ACCESSIBILITY_AUDIT.md"
    "SCHEMA_VALIDATION.md"
    "GSC_SETUP.md"
    "CONTENT_STRATEGY.md"
    "PORTFOLIO_AUDIT.md"
)

for file in "${DOC_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "⚠️  Optional: $file"
    fi
done

echo ""
echo "Checking SEO markup..."
for file in index.html about.html blog/index.html projects-enhanced.html portfolio.html docs/index.html docs/research.html; do
    if grep -q "application/ld+json" "$file" 2>/dev/null; then
        echo "✅ Schema markup in $file"
    else
        echo "⚠️  No schema markup in $file"
    fi
done

echo ""
echo "Checking HTML validity..."
for file in *.html blog/*.html docs/*.html 2>/dev/null; do
    if [ -f "$file" ]; then
        if grep -q "<!DOCTYPE html>" "$file" 2>/dev/null; then
            echo "✅ Valid DOCTYPE in $file"
        else
            echo "⚠️  Invalid DOCTYPE in $file"
        fi
    fi
done

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ All validations passed!"
    exit 0
else
    echo "❌ $ERRORS validation errors found"
    exit 1
fi

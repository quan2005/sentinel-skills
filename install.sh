#!/bin/bash

# Slidev Presentation Skill Installation Script
# This script installs the slidev presentation skill into Claude Code

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Claude Code directory exists
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"

if [ ! -d "$CLAUDE_DIR" ]; then
    print_error "Claude Code directory not found at $CLAUDE_DIR"
    print_error "Please make sure Claude Code is installed and has been run at least once"
    exit 1
fi

# Create skills directory if it doesn't exist
if [ ! -d "$SKILLS_DIR" ]; then
    print_status "Creating skills directory at $SKILLS_DIR"
    mkdir -p "$SKILLS_DIR"
fi

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_FILE="$SCRIPT_DIR/slidev-presentation-creator.md"
TARGET_FILE="$SKILLS_DIR/slidev-presentation-creator.md"

# Check if skill file exists
if [ ! -f "$SKILL_FILE" ]; then
    print_error "Skill file not found at $SKILL_FILE"
    print_error "Please run this script from the slidev-presentation-skill directory"
    exit 1
fi

# Check if skill already exists
if [ -f "$TARGET_FILE" ]; then
    print_warning "Skill already exists at $TARGET_FILE"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_status "Installation cancelled"
        exit 0
    fi
fi

# Copy the skill file
print_status "Installing slidev presentation skill..."
cp "$SKILL_FILE" "$TARGET_FILE"

# Verify installation
if [ -f "$TARGET_FILE" ]; then
    print_success "Skill installed successfully!"
    print_status "Skill location: $TARGET_FILE"

    echo
    print_status "Usage examples:"
    echo "  /slidev create \"My Presentation\""
    echo "  /slidev create \"Tech Talk\" --theme \"seriph\""
    echo "  /slidev create \"Demo\" --template \"company\""

    echo
    print_status "The skill will be available the next time you start Claude Code"
    print_status "If Claude Code is already running, you may need to restart it"

else
    print_error "Installation failed"
    exit 1
fi
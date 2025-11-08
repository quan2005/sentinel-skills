#!/bin/bash

# Skill Installation Template
# Modify this template for your specific skill installation needs

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SKILL_NAME="{{SKILL_NAME}}"
SKILL_VERSION="{{SKILL_VERSION}}"
INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"

echo -e "${BLUE}Installing $SKILL_NAME v$SKILL_VERSION...${NC}"

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo -e "${RED}Error: Claude Code is not installed or not in PATH${NC}"
    echo -e "${YELLOW}Please install Claude Code first: https://claude.ai/claude-code${NC}"
    exit 1
fi

# Create installation directory
echo -e "${BLUE}Creating installation directory...${NC}"
mkdir -p "$INSTALL_DIR"

# Copy skill files
echo -e "${BLUE}Installing skill files...${NC}"
cp SKILL.md "$INSTALL_DIR/"
cp package.json "$INSTALL_DIR/" 2>/dev/null || echo -e "${YELLOW}Warning: package.json not found${NC}"

# Copy any additional files your skill needs
# cp -r lib/ "$INSTALL_DIR/" 2>/dev/null || true
# cp -r templates/ "$INSTALL_DIR/" 2>/dev/null || true

# Install dependencies if needed
if [ -f "package.json" ] && grep -q '"dependencies"' "package.json"; then
    echo -e "${BLUE}Installing dependencies...${NC}"
    (cd "$INSTALL_DIR" && npm install --production)
fi

# Set up any configuration files
# echo -e "${BLUE}Setting up configuration...${NC}"
# mkdir -p "$HOME/.config/$SKILL_NAME"
# cp config/default.json "$HOME/.config/$SKILL_NAME/" 2>/dev/null || true

# Create executable scripts if needed
# if [ -f "bin/$SKILL_NAME" ]; then
#     echo -e "${BLUE}Installing executable...${NC}"
#     mkdir -p "$HOME/.local/bin"
#     cp "bin/$SKILL_NAME" "$HOME/.local/bin/"
#     chmod +x "$HOME/.local/bin/$SKILL_NAME"
#     echo -e "${YELLOW}Note: Make sure \$HOME/.local/bin is in your PATH${NC}"
# fi

# Add any post-installation setup
# echo -e "${BLUE}Running post-installation setup...${NC}"
# [Your setup commands here]

# Verify installation
echo -e "${BLUE}Verifying installation...${NC}"
if [ -f "$INSTALL_DIR/SKILL.md" ]; then
    echo -e "${GREEN}✓ Skill files installed successfully${NC}"
else
    echo -e "${RED}✗ Skill installation failed${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 $SKILL_NAME has been installed successfully!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Restart Claude Code"
echo "2. The skill will be available in your Claude Code session"
echo ""
echo -e "${BLUE}Skill location: $INSTALL_DIR${NC}"
echo -e "${BLUE}Documentation: $INSTALL_DIR/SKILL.md${NC}"

# Add any skill-specific usage instructions
echo ""
echo -e "${BLUE}Usage example:${NC}"
echo "Ask Claude: '使用 $SKILL_NAME 来...'"

echo ""
echo -e "${GREEN}Installation complete!${NC}"
#!/bin/bash

# Personal Skills Installation Script
# Usage: ./install.sh [skill-name]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKETPLACE_DIR="$SCRIPT_DIR/marketplace/skills"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_usage() {
    echo "Usage: $0 [skill-name]"
    echo ""
    echo "Options:"
    echo "  skill-name    Install a specific skill"
    echo "  --all         Install all available skills"
    echo "  --list        List available skills"
    echo "  --help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 my-cool-skill"
    echo "  $0 --all"
    echo "  $0 --list"
}

list_skills() {
    echo -e "${BLUE}Available skills:${NC}"
    echo ""

    if [ ! -d "$MARKETPLACE_DIR" ]; then
        echo -e "${YELLOW}No skills directory found${NC}"
        return 1
    fi

    for skill_dir in "$MARKETPLACE_DIR"/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            skill_doc="$skill_dir/SKILL.md"

            if [ -f "$skill_doc" ]; then
                # Extract first line from SKILL.md as description
                description=$(head -n 1 "$skill_doc" | sed 's/^# //')
                echo -e "  ${GREEN}$skill_name${NC} - $description"
            else
                echo -e "  ${YELLOW}$skill_name${NC} - (no documentation)"
            fi
        fi
    done
}

install_skill() {
    local skill_name="$1"
    local skill_dir="$MARKETPLACE_DIR/$skill_name"

    if [ ! -d "$skill_dir" ]; then
        echo -e "${RED}Error: Skill '$skill_name' not found${NC}"
        echo -e "${YELLOW}Available skills:${NC}"
        list_skills
        return 1
    fi

    local install_script="$skill_dir/install.sh"

    if [ ! -f "$install_script" ]; then
        echo -e "${RED}Error: No install script found for skill '$skill_name'${NC}"
        return 1
    fi

    echo -e "${BLUE}Installing skill: $skill_name${NC}"

    # Make install script executable and run it
    chmod +x "$install_script"
    (cd "$skill_dir" && ./install.sh)

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Successfully installed skill: $skill_name${NC}"
    else
        echo -e "${RED}✗ Failed to install skill: $skill_name${NC}"
        return 1
    fi
}

install_all_skills() {
    echo -e "${BLUE}Installing all available skills...${NC}"
    echo ""

    if [ ! -d "$MARKETPLACE_DIR" ]; then
        echo -e "${RED}Error: No skills directory found${NC}"
        return 1
    fi

    local installed_count=0
    local failed_count=0

    for skill_dir in "$MARKETPLACE_DIR"/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")

            if install_skill "$skill_name"; then
                ((installed_count++))
            else
                ((failed_count++))
            fi
            echo ""
        fi
    done

    echo -e "${GREEN}Installation summary:${NC}"
    echo -e "  ${GREEN}✓ Successfully installed: $installed_count${NC} skills"
    if [ $failed_count -gt 0 ]; then
        echo -e "  ${RED}✗ Failed to install: $failed_count${NC} skills"
    fi
}

# Main script logic
case "${1:-}" in
    --help|-h)
        print_usage
        ;;
    --list|-l)
        list_skills
        ;;
    --all|-a)
        install_all_skills
        ;;
    "")
        echo -e "${YELLOW}No skill specified. Use --all to install all skills or --list to see available skills.${NC}"
        echo ""
        print_usage
        ;;
    *)
        install_skill "$1"
        ;;
esac
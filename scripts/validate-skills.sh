#!/bin/bash

# Skills Validation Script
# Validates skill structure and documentation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/../skills"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_validation_header() {
    echo -e "${BLUE}Validating skills...${NC}"
    echo ""
}

validate_skill() {
    local skill_name="$1"
    local skill_dir="$SKILLS_DIR/$skill_name"
    local errors=0
    local warnings=0

    echo -e "${BLUE}Validating skill: $skill_name${NC}"

    # Check required files
    if [ ! -f "$skill_dir/SKILL.md" ]; then
        echo -e "  ${RED}✗ Missing SKILL.md${NC}"
        ((errors++))
    else
        echo -e "  ${GREEN}✓ SKILL.md exists${NC}"

        # Validate SKILL.md structure
        if ! grep -q "^# " "$skill_dir/SKILL.md"; then
            echo -e "  ${YELLOW}⚠ SKILL.md missing title${NC}"
            ((warnings++))
        fi
    fi

    if [ ! -f "$skill_dir/install.sh" ]; then
        echo -e "  ${RED}✗ Missing install.sh${NC}"
        ((errors++))
    else
        echo -e "  ${GREEN}✓ install.sh exists${NC}"

        # Check if install.sh is executable
        if [ ! -x "$skill_dir/install.sh" ]; then
            echo -e "  ${YELLOW}⚠ install.sh is not executable${NC}"
            ((warnings++))
        fi
    fi

    if [ ! -f "$skill_dir/package.json" ]; then
        echo -e "  ${YELLOW}⚠ Missing package.json (recommended)${NC}"
        ((warnings++))
    else
        echo -e "  ${GREEN}✓ package.json exists${NC}"
    fi

    # Check for common issues
    if [ -f "$skill_dir/install.sh" ]; then
        # Check for common install script issues
        if grep -q "rm -rf /" "$skill_dir/install.sh"; then
            echo -e "  ${RED}✗ Dangerous command found in install.sh${NC}"
            ((errors++))
        fi

        if ! grep -q "#!" "$skill_dir/install.sh"; then
            echo -e "  ${YELLOW}⚠ install.sh missing shebang${NC}"
            ((warnings++))
        fi
    fi

    # Summary
    if [ $errors -eq 0 ]; then
        echo -e "  ${GREEN}✓ Skill validation passed${NC}"
    else
        echo -e "  ${RED}✗ Skill validation failed with $errors error(s)${NC}"
    fi

    if [ $warnings -gt 0 ]; then
        echo -e "  ${YELLOW}⚠ $warnings warning(s)${NC}"
    fi

    echo ""

    return $errors
}

validate_all_skills() {
    local total_errors=0
    local total_warnings=0

    if [ ! -d "$SKILLS_DIR" ]; then
        echo -e "${RED}Error: No skills directory found${NC}"
        return 1
    fi

    for skill_dir in "$SKILLS_DIR"/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            validate_skill "$skill_name"
            errors=$?

            ((total_errors += errors))
        fi
    done

    # Final summary
    echo -e "${BLUE}Validation Summary:${NC}"
    if [ $total_errors -eq 0 ]; then
        echo -e "  ${GREEN}✓ All skills passed validation${NC}"
    else
        echo -e "  ${RED}✗ Found $total_errors error(s) across all skills${NC}"
    fi

    if [ $total_warnings -gt 0 ]; then
        echo -e "  ${YELLOW}⚠ Found $total_warnings warning(s) across all skills${NC}"
    fi

    return $total_errors
}

# Main execution
print_validation_header
validate_all_skills
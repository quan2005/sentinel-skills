#!/bin/bash

# Slidev Skills Marketplace - Skills Validator
# 验证技能结构和内容质量

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "${BLUE}🔍=======================================🔍${NC}"
    echo -e "${BLUE}     Skills Validator${NC}"
    echo -e "${BLUE}🔍=======================================🔍${NC}"
    echo
}

# 验证技能文件结构
validate_skill_structure() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")

    print_info "验证技能结构: $skill_name"

    local errors=0

    # 检查 SKILL.md 文件
    if [ ! -f "$skill_path/SKILL.md" ]; then
        print_error "缺少 SKILL.md 文件"
        ((errors++))
    else
        print_success "✓ SKILL.md 文件存在"
    fi

    # 检查必需的元数据字段
    if [ -f "$skill_path/SKILL.md" ]; then
        local required_fields=("name:" "description:" "version:")
        for field in "${required_fields[@]}"; do
            if ! grep -q "^$field" "$skill_path/SKILL.md"; then
                print_error "缺少必需字段: $field"
                ((errors++))
            else
                print_success "✓ 找到字段: $field"
            fi
        done

        # 验证名称格式
        local name=$(grep "^name:" "$skill_path/SKILL.md" | cut -d'"' -f2)
        if [[ ! "$name" =~ ^[a-z0-9-]+$ ]]; then
            print_error "技能名称格式不正确: $name"
            ((errors++))
        else
            print_success "✓ 技能名称格式正确: $name"
        fi

        # 验证描述长度
        local description=$(grep "^description:" "$skill_path/SKILL.md" | cut -d'"' -f2)
        if [ ${#description} -gt 1024 ]; then
            print_warning "描述过长 (${#description} > 1024)"
            ((errors++))
        else
            print_success "✓ 描述长度符合要求 (${#description} <= 1024)"
        fi
    fi

    # 检查可选文件
    if [ -f "$skill_path/README.md" ]; then
        print_success "✓ README.md 文件存在"
    else
        print_warning "⚠️ 建议添加 README.md 文件"
    fi

    if [ -d "$skill_path/examples" ]; then
        print_success "✓ examples 目录存在"
    else
        print_warning "⚠️ 建议添加 examples 目录"
    fi

    if [ -d "$skill_path/templates" ]; then
        print_success "✓ templates 目录存在"
    else
        print_warning "⚠️ 建议添加 templates 目录"
    fi

    return $errors
}

# 验证技能内容质量
validate_skill_content() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")

    print_info "验证技能内容质量: $skill_name"

    local errors=0

    # 检查是否包含图文并茂相关内容
    local skill_file="$skill_path/SKILL.md"
    if [ -f "$skill_file" ]; then
        # 检查是否包含"图文并茂"
        if grep -q "图文并茂" "$skill_file"; then
            print_success "✓ 包含图文并茂要求"
        else
            print_warning "⚠️ 未明确提及图文并茂要求"
        fi

        # 检查是否包含详细的使用说明
        local content_lines=$(wc -l < "$skill_file")
        if [ "$content_lines" -lt 50 ]; then
            print_warning "⚠️ 内容较少 ($content_lines 行)，建议添加更多细节"
            ((errors++))
        else
            print_success "✓ 内容充实 ($content_lines 行)"
        fi

        # 检查是否包含示例
        if grep -q "```" "$skill_file"; then
            print_success "✓ 包含代码示例"
        else
            print_warning "⚠️ 建议添加代码示例"
        fi

        # 检查是否包含最佳实践
        if grep -q "最佳实践\|最佳方式\|注意事项" "$skill_file"; then
            print_success "✓ 包含最佳实践指导"
        else
            print_warning "⚠️ 建议添加最佳实践指导"
        fi
    fi

    return $errors
}

# 验证技能文件完整性
validate_skill_files() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")

    print_info "验证技能文件完整性: $skill_name"

    local errors=0

    # 验证所有 Markdown 文件
    find "$skill_path" -name "*.md" -type f | while read -r file; do
        if ! grep -q "^#" "$file"; then
            print_warning "⚠️ 文件缺少标题: $file"
            ((errors++))
        fi
    done

    # 检查脚本文件权限
    find "$skill_path" -name "*.sh" -type f | while read -r file; do
        if [ ! -x "$file" ]; then
            print_warning "⚠️ 脚本文件不可执行: $file"
            ((errors++))
        fi
    done

    return $errors
}

# 主验证函数
main() {
    print_header

    local marketplace_dir="./marketplace"
    local skills_dir="$marketplace_dir/skills"
    local total_errors=0

    if [ ! -d "$skills_dir" ]; then
        print_error "技能目录不存在: $skills_dir"
        exit 1
    fi

    print_info "开始验证所有技能..."
    echo

    local skill_count=0

    for skill_path in "$skills_dir"/*; do
        if [ -d "$skill_path" ]; then
            local skill_name=$(basename "$skill_path")
            echo
            print_info "验证技能: $skill_name"
            echo "----------------------------------------"

            # 验证结构
            local structure_errors=$(validate_skill_structure "$skill_path")

            # 验证内容
            local content_errors=$(validate_skill_content "$skill_path")

            # 验证文件完整性
            local file_errors=$(validate_skill_files "$skill_path")

            local total_skill_errors=$((structure_errors + content_errors + file_errors))

            if [ $total_skill_errors -eq 0 ]; then
                print_success "🎉 技能 '$skill_name' 验证通过"
            else
                print_error "❌ 技能 '$skill_name' 验证失败 ($total_skill_errors 个错误)"
            fi

            total_errors=$((total_errors + total_skill_errors))
            ((skill_count++))
        fi
    done

    echo
    print_header
    echo "验证结果:"
    echo "----------------------------------------"
    echo -e "总技能数: $skill_count"
    echo -e "错误总数: $total_errors"
    echo

    if [ $total_errors -eq 0 ]; then
        print_success "🎉 所有技能验证通过！"
        exit 0
    else
        print_error "❌ 发现 $total_errors 个错误，请修复后重试"
        exit 1
    fi
}

# 运行验证
main "$@"
#!/bin/bash

# Slidev Skills Marketplace - Skill Installer
# 安装指定的技能到 Claude Code

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 打印带颜色的消息
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
    echo -e "${PURPLE}🌟=======================================🌟${NC}"
    echo -e "${PURPLE}     Slidev Skills Marketplace${NC}"
    echo -e "${PURPLE}         Skill Installer${NC}"
    echo -e "${PURPLE}🌟=======================================🌟${NC}"
    echo
}

# 显示帮助信息
show_help() {
    cat << EOF
用法: $0 [选项] <技能名称>

选项:
  -h, --help              显示此帮助信息
  -l, --list              列出所有可用技能
  -f, --force             强制覆盖已存在的技能
  -v, --verbose           详细输出
  -c, --check             只检查技能是否已安装
  -u, --uninstall         卸载指定的技能
  --list-installed        列出已安装的技能
  --marketplace-dir DIR   指定市场目录 (默认: ./marketplace)
  --claude-dir DIR        指定 Claude 技能目录 (默认: ~/.claude/skills)

示例:
  $0 slidev-presentation-creator     安装演示文稿创建器技能
  $0 -l                               列出所有可用技能
  $0 -c slidev-presentation-creator  检查技能是否已安装
  $0 -u slidev-presentation-creator  卸载技能

更多信息请访问: https://github.com/your-username/slidev-presentation-skill
EOF
}

# 默认配置
MARKETPLACE_DIR="./marketplace"
CLAUDE_DIR="$HOME/.claude/skills"
FORCE_INSTALL=false
VERBOSE=false
CHECK_ONLY=false
UNINSTALL=false
LIST_INSTALLED=false

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -l|--list)
            LIST_SKILLS=true
            shift
            ;;
        -f|--force)
            FORCE_INSTALL=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -c|--check)
            CHECK_ONLY=true
            shift
            ;;
        -u|--uninstall)
            UNINSTALL=true
            shift
            ;;
        --list-installed)
            LIST_INSTALLED=true
            shift
            ;;
        --marketplace-dir)
            MARKETPLACE_DIR="$2"
            shift 2
            ;;
        --claude-dir)
            CLAUDE_DIR="$2"
            shift 2
            ;;
        -*)
            print_error "未知选项: $1"
            echo "使用 -h 或 --help 查看帮助信息"
            exit 1
            ;;
        *)
            SKILL_NAME="$1"
            shift
            ;;
    esac
done

# 详细输出函数
verbose() {
    if [ "$VERBOSE" = true ]; then
        echo -e "${CYAN}🔧 $1${NC}"
    fi
}

# 检查依赖
check_dependencies() {
    verbose "检查系统依赖..."

    # 检查基本命令
    for cmd in cp rm mkdir find; do
        if ! command -v "$cmd" &> /dev/null; then
            print_error "缺少必需的命令: $cmd"
            exit 1
        fi
    done

    # 检查 Claude 技能目录
    if [ ! -d "$CLAUDE_DIR" ]; then
        print_warning "Claude 技能目录不存在，将自动创建: $CLAUDE_DIR"
        mkdir -p "$CLAUDE_DIR"
    fi

    verbose "依赖检查完成"
}

# 列出可用技能
list_skills() {
    print_header
    print_info "可用的技能:"
    echo

    if [ ! -d "$MARKETPLACE_DIR/skills" ]; then
        print_error "市场目录不存在: $MARKETPLACE_DIR/skills"
        exit 1
    fi

    local count=0
    for skill_dir in "$MARKETPLACE_DIR/skills"/*; do
        if [ -d "$skill_dir" ]; then
            local skill_name=$(basename "$skill_dir")
            local skill_file="$skill_dir/SKILL.md"

            if [ -f "$skill_file" ]; then
                local description=$(grep "^description:" "$skill_file" | cut -d'"' -f2 | cut -d',' -f1)
                local version=$(grep "^version:" "$skill_file" | cut -d'"' -f2)

                echo -e "${GREEN}📦 $skill_name${NC}"
                echo -e "   📝 描述: $description"
                echo -e "   🏷️  版本: $version"

                # 检查是否已安装
                if [ -d "$CLAUDE_DIR/$skill_name" ]; then
                    echo -e "   ${GREEN}✅ 已安装${NC}"
                else
                    echo -e "   ${YELLOW}⭕ 未安装${NC}"
                fi
                echo
                ((count++))
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        print_warning "未找到任何技能"
    else
        print_success "共找到 $count 个技能"
    fi
}

# 列出已安装技能
list_installed_skills() {
    print_header
    print_info "已安装的技能:"
    echo

    if [ ! -d "$CLAUDE_DIR" ]; then
        print_error "Claude 技能目录不存在: $CLAUDE_DIR"
        exit 1
    fi

    local count=0
    for skill_dir in "$CLAUDE_DIR"/*; do
        if [ -d "$skill_dir" ]; then
            local skill_name=$(basename "$skill_dir")
            local skill_file="$skill_dir/SKILL.md"

            if [ -f "$skill_file" ]; then
                local description=$(grep "^description:" "$skill_file" | cut -d'"' -f2 | cut -d',' -f1)
                local version=$(grep "^version:" "$skill_file" | cut -d'"' -f2)

                echo -e "${GREEN}📦 $skill_name${NC}"
                echo -e "   📝 描述: $description"
                echo -e "   🏷️  版本: $version"
                echo
                ((count++))
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        print_warning "未找到已安装的技能"
    else
        print_success "共找到 $count 个已安装技能"
    fi
}

# 验证技能
validate_skill() {
    local skill_path="$1"
    verbose "验证技能: $skill_path"

    # 检查技能目录
    if [ ! -d "$skill_path" ]; then
        print_error "技能目录不存在: $skill_path"
        return 1
    fi

    # 检查 SKILL.md 文件
    local skill_file="$skill_path/SKILL.md"
    if [ ! -f "$skill_file" ]; then
        print_error "技能文件不存在: $skill_file"
        return 1
    fi

    # 检查必需的前置元数据字段
    local required_fields=("name:" "description:" "version:")
    for field in "${required_fields[@]}"; do
        if ! grep -q "^$field" "$skill_file"; then
            print_error "缺少必需字段: $field"
            return 1
        fi
    done

    verbose "技能验证通过"
    return 0
}

# 检查技能是否已安装
check_skill_installed() {
    local skill_name="$1"
    local installed_path="$CLAUDE_DIR/$skill_name"

    if [ -d "$installed_path" ]; then
        if validate_skill "$installed_path"; then
            print_success "技能 '$skill_name' 已安装"
            return 0
        else
            print_warning "技能 '$skill_name' 已安装但验证失败"
            return 1
        fi
    else
        print_warning "技能 '$skill_name' 未安装"
        return 1
    fi
}

# 安装技能
install_skill() {
    local skill_name="$1"
    local source_path="$MARKETPLACE_DIR/skills/$skill_name"
    local target_path="$CLAUDE_DIR/$skill_name"

    verbose "准备安装技能: $skill_name"
    verbose "源路径: $source_path"
    verbose "目标路径: $target_path"

    # 检查技能是否存在
    if [ ! -d "$source_path" ]; then
        print_error "技能不存在: $skill_name"
        print_info "使用 '$0 -l' 查看可用技能列表"
        exit 1
    fi

    # 验证技能
    if ! validate_skill "$source_path"; then
        print_error "技能验证失败: $skill_name"
        exit 1
    fi

    # 检查是否已安装
    if [ -d "$target_path" ]; then
        if [ "$FORCE_INSTALL" = false ]; then
            print_warning "技能 '$skill_name' 已安装"
            print_info "使用 -f 选项强制覆盖"
            return 0
        else
            print_warning "覆盖已安装的技能: $skill_name"
            rm -rf "$target_path"
        fi
    fi

    # 复制技能文件
    verbose "复制技能文件..."
    cp -r "$source_path" "$CLAUDE_DIR/"

    # 验证安装
    if validate_skill "$target_path"; then
        print_success "技能 '$skill_name' 安装成功!"

        # 显示技能信息
        local skill_file="$target_path/SKILL.md"
        local description=$(grep "^description:" "$skill_file" | cut -d'"' -f2 | cut -d',' -f1)
        local version=$(grep "^version:" "$skill_file" | cut -d'"' -f2)

        echo
        print_info "技能信息:"
        echo -e "   📦 名称: $skill_name"
        echo -e "   📝 描述: $description"
        echo -e "   🏷️  版本: $version"
        echo -e "   📍 位置: $target_path"
        echo
        print_info "现在您可以在 Claude Code 中使用此技能了!"

    else
        print_error "技能安装验证失败"
        # 清理失败的安装
        rm -rf "$target_path"
        exit 1
    fi
}

# 卸载技能
uninstall_skill() {
    local skill_name="$1"
    local target_path="$CLAUDE_DIR/$skill_name"

    verbose "准备卸载技能: $skill_name"
    verbose "目标路径: $target_path"

    if [ ! -d "$target_path" ]; then
        print_warning "技能 '$skill_name' 未安装"
        return 0
    fi

    # 确认卸载
    if [ "$FORCE_INSTALL" = false ]; then
        echo -n "确定要卸载技能 '$skill_name' 吗? [y/N]: "
        read -r response
        case "$response" in
            [yY][eE][sS]|[yY])
                ;;
            *)
                print_info "取消卸载"
                return 0
                ;;
        esac
    fi

    # 卸载技能
    verbose "删除技能文件..."
    rm -rf "$target_path"

    print_success "技能 '$skill_name' 卸载成功"
}

# 主函数
main() {
    print_header

    # 检查依赖
    check_dependencies

    # 显示配置信息
    if [ "$VERBOSE" = true ]; then
        echo -e "${CYAN}配置信息:${NC}"
        echo -e "   市场目录: $MARKETPLACE_DIR"
        echo -e "   Claude 目录: $CLAUDE_DIR"
        echo
    fi

    # 执行相应操作
    if [ "$LIST_SKILLS" = true ]; then
        list_skills
    elif [ "$LIST_INSTALLED" = true ]; then
        list_installed_skills
    elif [ -n "$SKILL_NAME" ]; then
        if [ "$CHECK_ONLY" = true ]; then
            check_skill_installed "$SKILL_NAME"
            exit $?
        elif [ "$UNINSTALL" = true ]; then
            uninstall_skill "$SKILL_NAME"
        else
            install_skill "$SKILL_NAME"
        fi
    else
        print_error "请指定要安装的技能名称"
        echo
        show_help
        exit 1
    fi
}

# 运行主函数
main "$@"
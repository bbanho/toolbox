#!/bin/bash
# GitHub commands script for PYX Engenharia portfolio

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required commands
check_requirements() {
    local missing=()
    
    for cmd in git gh; do
        if ! command_exists "$cmd"; then
            missing+=("$cmd")
        fi
    done
    
    if [ ${#missing[@]} -ne 0 ]; then
        print_message "$RED" "Error: The following required commands are missing:"
        printf '%s\n' "${missing[@]}"
        exit 1
    fi
}

# Function to create a new feature branch
create_feature_branch() {
    local branch_name=$1
    
    if [ -z "$branch_name" ]; then
        print_message "$RED" "Error: Branch name is required"
        echo "Usage: $0 create-branch <branch-name>"
        exit 1
    fi
    
    # Ensure we're on main branch and it's up to date
    git checkout main
    git pull origin main
    
    # Create and switch to new branch
    git checkout -b "feature/$branch_name"
    print_message "$GREEN" "Created and switched to feature/$branch_name"
}

# Function to create a pull request
create_pull_request() {
    local title=$1
    local body=$2
    
    if [ -z "$title" ]; then
        print_message "$RED" "Error: PR title is required"
        echo "Usage: $0 create-pr <title> [body]"
        exit 1
    fi
    
    # Get current branch name
    local branch=$(git symbolic-ref --short HEAD)
    
    # Create PR
    gh pr create --title "$title" --body "${body:-$title}" --base main
    
    print_message "$GREEN" "Created pull request for $branch"
}

# Function to deploy to GitHub Pages
deploy_pages() {
    # Ensure we're on main branch
    if [ "$(git symbolic-ref --short HEAD)" != "main" ]; then
        print_message "$RED" "Error: Must be on main branch to deploy"
        exit 1
    fi
    
    # Pull latest changes
    git pull origin main
    
    # Deploy to GitHub Pages
    gh pages deploy .
    
    print_message "$GREEN" "Deployed to GitHub Pages"
}

# Function to show help
show_help() {
    echo "PYX Engenharia Portfolio GitHub Commands"
    echo
    echo "Usage: $0 <command> [options]"
    echo
    echo "Commands:"
    echo "  create-branch <name>    Create a new feature branch"
    echo "  create-pr <title> [body] Create a pull request"
    echo "  deploy                  Deploy to GitHub Pages"
    echo "  help                    Show this help message"
}

# Main script
check_requirements

case "$1" in
    "create-branch")
        create_feature_branch "$2"
        ;;
    "create-pr")
        create_pull_request "$2" "$3"
        ;;
    "deploy")
        deploy_pages
        ;;
    "help"|"")
        show_help
        ;;
    *)
        print_message "$RED" "Error: Unknown command '$1'"
        show_help
        exit 1
        ;;
esac 
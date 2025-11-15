#!/bin/bash
source "$(dirname "$0")/github_release.sh"
source "$(dirname "$0")/vim_org_release.sh"

set -e
echo -n "Release to Github/Vim.org? > "
read -r source_choice

choice="${source_choice,,}"

if [[ "$choice" == "github" ]]; then
  github_release
elif [[ "$choice" == "vim.org" ]]; then
  vim_org_release
else
  echo "unknown option: $source_choice"
fi

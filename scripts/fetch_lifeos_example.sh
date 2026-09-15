#!/usr/bin/env bash
set -euo pipefail

# Fetch the upstream example vault as a separate, untracked reference checkout.
# Do not copy its plugin state, sample notes, or assets into this public repo.
source_url=https://github.com/quanru/obsidian-example-lifeos.git
source_commit=80fb5649d6081e37b661ae3b6d4d77943921915a
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
reference_dir="$project_root/.reference/lifeos-example"

if [[ ! -d "$reference_dir/.git" ]]; then
  mkdir -p "$project_root/.reference"
  git clone --no-checkout "$source_url" "$reference_dir"
fi

git -C "$reference_dir" fetch origin "$source_commit"
git -C "$reference_dir" checkout --detach "$source_commit"

printf 'Upstream example is available at %s (%s)\n' "$reference_dir" "$source_commit"

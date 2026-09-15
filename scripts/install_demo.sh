#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixtures="$project_root/demo/fixtures"
if [[ ! -d "$fixtures" ]]; then
  printf 'Missing fixtures: %s\n' "$fixtures" >&2
  exit 1
fi

# Preflight every path before writing anything. Never overwrite a real note.
while IFS= read -r -d '' source_file; do
  relative_path="${source_file#"$fixtures"/}"
  target_file="$project_root/$relative_path"
  if [[ -e "$target_file" ]]; then
    printf 'Refusing to overwrite existing note: %s\n' "$target_file" >&2
    exit 1
  fi
done < <(find "$fixtures" -type f -print0)

while IFS= read -r -d '' source_file; do
  relative_path="${source_file#"$fixtures"/}"
  target_file="$project_root/$relative_path"
  mkdir -p "$(dirname "$target_file")"
  cp -- "$source_file" "$target_file"
  printf 'Installed %s\n' "$relative_path"
done < <(find "$fixtures" -type f -print0)

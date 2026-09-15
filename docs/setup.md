# Reproduce and migrate

1. Clone this repository as a separate Obsidian vault. It is public and contains only templates and synthetic material; keep your internal vault separate.
2. Enable your existing `periodic-para` (LifeOS), Dataview, and Templater plugins in the local copy. Do not commit the copied `.obsidian` directory or plugin data. Configure Templater's folder to `Templates`.
3. Let LifeOS create daily and weekly notes in a throwaway copy. Inspect its actual settings, generated note names, `Daily Record` heading, and the installed daily/weekly templates. Compare its defaults with `Templates/Daily.md` and `Templates/Weekly.md`; do not overwrite templates blindly.
4. Point your homepage plugin at `HOME.md` if useful. The Dataview queries assume notes in `4. Management`. The other installed plugins remain optional: QuickAdd may improve capture later, Tasks is for personal commitments only, and Obsidian Git should push only synthetic or approved content.
5. For a deterministic aggregation experiment, use `python3 scripts/weekly_signals.py "0. PeriodicNotes/Daily" --week 2026-W38` after adjusting the daily folder to match LifeOS. It expects notes named `YYYY-MM-DD.md`, collects non-task bullets under `## Daily Record`, and prints links to each source day. It reads local files only.
6. Run `python3 -m unittest discover -s tests` to validate the helper. Work from a copy when mapping internal content; review confidentiality before transferring even a sanitized note into this public repository.

The Obsidian CLI is useful for checking live plugin commands and opening notes on your workstation. This repo setup does not rely on CLI availability in a headless GitHub environment.

# Reproduce and migrate

1. Clone this repository as a separate Obsidian vault. It is public and contains only templates and synthetic material; keep your internal vault separate.
2. Enable your existing `periodic-para` (LifeOS), Dataview, and Templater plugins in the local copy. Do not commit the copied `.obsidian` directory or plugin data. The Daily and Weekly drafts are at LifeOS's example-path `0. PeriodicNotes/Templates/`; the management templates remain in `Templates/` for optional Templater use.
3. Let LifeOS create daily and weekly notes in a throwaway copy. Inspect its settings for daily/weekly folder and file formats, template paths, and Daily Record heading. Your vault is based on the example project, whose source templates live in `0. PeriodicNotes/Templates/`. Compare those templates with these drafts and selectively merge sections rather than replacing the originals. The example LifeOS settings use `periodicNotesPath: "0. PeriodicNotes"` and `dailyRecordHeader: "Daily Record"`; its Daily Notes setting uses `YYYY/[Daily]/MM/YYYY-MM-DD`.
4. Keep `## Daily Record` in the daily note, with plain bullets for safe observations. The weekly note's `LifeOS` / `BulletRecordListByTime` block displays the collected bullets when LifeOS and Dataview are active. It is a live view; it does not copy its rendered output into a Markdown file for an external LLM. Human review or a later explicit export is still needed for that.
5. Point your homepage plugin at `HOME.md` if useful. The Dataview queries assume notes in `4. Management`. The other installed plugins remain optional: QuickAdd may improve capture later, Tasks is for personal commitments only, and Obsidian Git should push only synthetic or approved content.
6. Work from a copy when mapping internal content; review confidentiality before transferring even a sanitized note into this public repository. The Obsidian CLI can help inspect live plugin commands and open notes on your workstation; this GitHub-based scaffold cannot access your local running app.

Source templates: [Daily](https://github.com/quanru/obsidian-example-lifeos/blob/main/0.%20PeriodicNotes/Templates/Daily.md), [Weekly](https://github.com/quanru/obsidian-example-lifeos/blob/main/0.%20PeriodicNotes/Templates/Weekly.md).

## Local upstream reference

Run `bash scripts/fetch_lifeos_example.sh` to clone the upstream English example vault at a pinned commit into `.reference/lifeos-example/`. That directory is ignored by Git. Compare its `0. PeriodicNotes/Templates/`, `1. Projects/`, `2. Areas/`, `3. Resources/`, and tracked `.obsidian/` files with your local installation. The upstream checkout is detached; use an explicit local branch if you want to experiment inside it. This does not merge or publish upstream files into our public repository.

For a one-week synthetic rendering check, follow [the demo walkthrough](../demo/README.md). Run its installer only in a fresh local checkout; it refuses to overwrite existing notes.

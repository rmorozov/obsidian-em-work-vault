# Synthetic one-week walkthrough

Open the repository root as a separate Obsidian vault. Enable your locally installed LifeOS (`periodic-para`) and Dataview plugins. The repository has LifeOS Daily and Weekly drafts at `0. PeriodicNotes/Templates/`; it intentionally does not distribute plugin binaries or real settings.

Run `bash scripts/install_demo.sh` from the repository root. The script checks for existing target paths before writing and refuses to replace any note. It installs synthetic notes for ISO week `2026-W38` into LifeOS's default nested paths, along with three management notes. The live copies are ignored by Git.

Open `0. PeriodicNotes/2026/Weekly/2026-W38.md` in Obsidian. Under **Daily signals**, expect six plain bullets from Monday, Wednesday and Friday, with source links. The two task checkboxes and the bullet under **Other** should not appear. Open `HOME.md`: expect one open decision, one open risk and one observed systemic problem. Move the risk's `status` to `closed` locally to check that it drops out of the open-risk query.

The weekly block is a **live view**; its rendered bullets do not become text in the Markdown source. Check your local LifeOS settings for `periodicNotesPath`, `dailyRecordHeader`, and date formats if the view is empty. The upstream example uses `0. PeriodicNotes` and `Daily Record`.

This demo establishes rendering and the manual review loop. It does not validate QuickAdd capture, automatic note generation, or LLM export.

# Obsidian Engineering Manager Work Vault

A public, sample-only experiment for a lightweight management review workflow built around LifeOS (`periodic-para`), PARA, daily capture and weekly review.

Start with [the design brief](docs/design.md) and [local setup steps](docs/setup.md). `Templates/` contains small management note and periodic note drafts; `HOME.md` contains Dataview management views. The weekly template reuses LifeOS `BulletRecordListByTime` for live collection of Daily Record bullets.

The real vault, actual daily/weekly notes, personal notes and `.obsidian` settings should be kept out of this public repository. Verify LifeOS's generated templates and settings in a local throwaway copy before migrating internal content.

For side-by-side comparison with the complete upstream example, run `bash scripts/fetch_lifeos_example.sh`; it creates an ignored, pinned local checkout under `.reference/`.

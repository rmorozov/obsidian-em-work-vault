# Synthetic one-week walkthrough

Open the repository root as a separate Obsidian vault. For the board experiment, use Obsidian 1.14+ and enable the core Bases plugin. Enable your locally installed LifeOS (`periodic-para`) and Dataview plugins. The repository has LifeOS Daily and Weekly drafts at `0. PeriodicNotes/Templates/`; it intentionally does not distribute plugin binaries or real settings.

Run `bash scripts/install_demo.sh` from the repository root. The script checks for existing target paths before writing and refuses to replace any note. It installs synthetic notes for ISO week `2026-W38` into LifeOS's default nested paths, along with three management notes. The live copies are ignored by Git.

Open `0. PeriodicNotes/2026/Weekly/2026-W38.md` in Obsidian. Under **Daily signals**, expect six plain bullets from Monday, Wednesday and Friday, with source links. The two task checkboxes and the bullet under **Other** should not appear. Open `HOME.md`: expect one open decision, one open risk and one observed systemic problem. The closure check is performed in step 5 below, after the three-card checks.

The weekly block is a **live view**; its rendered bullets do not become text in the Markdown source. Check your local LifeOS settings for `periodicNotesPath`, `dailyRecordHeader`, and date formats if the view is empty. The upstream example uses `0. PeriodicNotes` and `Daily Record`.

## Native Bases check

For a previous demo installation, use a fresh checkout to get the updated fixtures. The installer deliberately refuses to replace your existing sample notes and local edits. There is no force or migration step in this experiment.

Set property types as described in [the Bases guide](../docs/bases.md). Open HOME in Reading view, or open `4. Management/Management.base` directly and choose its named views.

| Attention column | Expected single card | Lifecycle status | Next checkpoint |
| --- | --- | --- | --- |
| Now | Release validation ownership | open | 2026-09-21 (needed_by) |
| This week | API review delay | open | 2026-09-21 (review_on) |
| Watch | Release coordination interruptions | observed | 2026-09-25 (review_on) |

1. Expect three cards, three Review dates rows, and an empty Attention needs correction table, without fixture or template duplicates. The two 21 September checkpoints precede 25 September; the tied rows sort by note name. Dates are intentionally fixed to the synthetic week, not the current date.
2. Move API review delay from This week to Now. Its frontmatter should change to `attention: Now` while `status: open` and `review_on` stay unchanged. Both the board and review table should update.
3. Edit the risk's `review_on` to `2026-09-26` in the table. The note and Dataview risk view should show the same date, and its checkpoint should sort after the systemic problem.
4. Remove the risk's `attention` in the note. It should appear in None, in Attention needs correction directly below the board, and in Review dates. Restore `This week`; the correction row should disappear. Then test a typo such as `This wek`: the risk is hidden by the board's explicit column list but must appear in Attention needs correction and Review dates. Correct it to `This week` in the correction table; it should return to the board and disappear from the correction table.
5. Set the risk's `status` to `closed`. It should disappear from both Bases views and the Dataview open-risk view. Restore `open` to reset the demo.
6. Confirm the weekly LifeOS view still contains the original six signals. Moving a card must not affect daily capture or weekly aggregation.

Record whether rendering, card movement, date editing and Dataview refresh worked, and which interface made the review easier. If Bases fails, the Dataview views remain below it and the weekly LifeOS check is independent.

This demo establishes rendering and the manual review loop. It does not validate QuickAdd capture, automatic note generation, or LLM export.

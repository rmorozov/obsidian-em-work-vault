# Bases attention experiment (Obsidian 1.14+)

The native board is an editable view of existing management notes. It complements LifeOS's weekly bullet aggregation and the Dataview tables in HOME. No community Kanban plugin is required for this experiment.

## Properties

Use Obsidian's property editor to set these types locally. This repository does not ship or overwrite `.obsidian` settings.

| Property | Obsidian type | Meaning |
| --- | --- | --- |
| `type` | Text | `decision`, `risk`, or `systemic-problem` |
| `status` | Text | Lifecycle progress; retain existing lowercase values |
| `attention` | Text | Exactly `Now`, `This week`, or `Watch` |
| `needed_by` | Date | Decision deadline, when known |
| `review_on` | Date | Next review, when known |

New management templates default to `Watch`; choose attention when promoting an item. There are no added fields or dialogs for daily bullets. A watching risk can deserve attention Now without changing its lifecycle status.

## Views

`4. Management/Management.base` contains three views, embedded in HOME:

- **Attention:** cards grouped by editable `note.attention`, ordered Now / This week / Watch / None. Cards display the note name, type, status and dates. Moving a card changes `attention`, not `status` or the note's folder.
- **Attention needs correction:** an editable table immediately below the board lists active notes whose attention is missing or differs from the three supported values. Correct the value in that table to return a hidden card to the board. With the initial fixtures it is empty.
- **Review dates:** the same active notes, with editable `review_on` and `needed_by` columns. A read-only Next checkpoint formula uses `review_on` when present, otherwise `needed_by`, and sorts earliest first. It is a review checkpoint, not a replacement for the decision deadline, which remains separately visible. Notes with no date remain in the table.

The shared filter includes only Markdown management notes under `4. Management`, and excludes `closed` and `resolved` items. Templates, raw daily notes and fixture originals under `demo/fixtures` are outside that folder and do not appear. The Dataview decision table still shows only `open` decisions; the attention view also retains later active stages such as `decided` and `communicated` until `closed`.

Missing attention appears in None and Attention needs correction. The explicit column order hides unsupported attention values; Attention needs correction surfaces these immediately below the board, and Review dates also retains them. Check the correction table before relying on the board when adopting or editing notes. Use the property spellings in the table above; do not introduce parallel `review` or `needed-by` fields.

Create promoted notes with the existing templates in their management folders. The board's plus button supplies a grouping value, but does not guarantee our type, lifecycle fields or body template; avoid using it for this first experiment.

## Validate in Obsidian

Follow [the demo walkthrough](../demo/README.md) for the expected cards, date order and property-edit checks. Live rendering, drag-and-drop persistence and Dataview refresh require the running app; YAML parsing alone cannot verify them.

After one week, compare how quickly you can identify the next intervention, change attention and find the next review date. Keep either interface or both based on that trial. LifeOS and Dataview remain required for native weekly signal aggregation.

References: [Bases syntax](https://obsidian.md/help/bases/syntax), [Kanban view](https://obsidian.md/help/bases/views/kanban), [embedding views](https://obsidian.md/help/bases/create-base).

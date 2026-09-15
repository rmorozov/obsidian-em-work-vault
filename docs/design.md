# Work vault v1 design brief

This captures the decisions from the planning chat for use in future repository sessions. It is a hypothesis to test against the actual local vault, not a transcription of private material.

## Information boundary

Human triage happens before capture. Put safe or deliberately sanitized summaries in this Work vault; keep sensitive people and confidential details in a separate private vault. A public GitHub experiment must use synthetic notes only. A corporate LLM receives only material that has already crossed the human boundary.

## Workflow

- PARA: Projects have a finishable outcome; Areas are ongoing responsibilities; Resources are reference; Archives are inactive.
- LifeOS (`periodic-para`) supplies periodic notes and PARA mechanics. Its `Daily Record` is the low-friction capture stream; a plain bullet is an observation, and a task checkbox is reserved for an actual personal commitment.
- The weekly review correlates daily observations with open decisions, risks, and recurring organizational problems. Most bullets should expire without promotion.
- Management objects record rationale, evidence, intervention triggers and review dates. ADO remains the execution tracker; link to items rather than copying their status.
- AI may suggest attention, patterns and omissions after human triage. The manager edits and owns the final weekly review and decisions.

## Reuse from the example vault

The source vault's `0. PeriodicNotes/Templates/Daily.md` has `## Daily Record` and a project snapshot. Its Weekly template uses the verified `LifeOS` code block `BulletRecordListByTime` under “Collected this week.” We retain the capture heading, optional project snapshot and bullet aggregation while simplifying the role, habit, time accounting and task views. The sample Project template provides tag-based task, bullet and file queries; we can selectively add those later if a concrete management question requires them.

LifeOS implements `BulletRecordListByTime` using Dataview: it gathers non-task list items from daily files in the period and filters by the configured Daily Record heading. The view is rendered dynamically in Obsidian. It is the native collection mechanism; no independent Python collector is needed for v1.

Inspect the locally installed LifeOS settings and date formats before migrating data or replacing a local template. Never overwrite existing LifeOS-created files during migration.

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

## Validate locally before migrating

The previous chat suggested LifeOS `BulletRecordListByTime` aggregation, but its exact template block syntax, the installed template paths, plugin settings, and date formats must be verified against the local installation. Do not paste a placeholder code fence into a production weekly template. The included independent helper offers a deterministic fallback during experiments.

The folder names in this repository are an experiment. Prefer mapping a copy of the real vault before moving any notes. Never overwrite existing LifeOS-created files during migration.

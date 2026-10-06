# Management cockpit

Open today's LifeOS daily note and capture safe observations under **Daily Record**. Review the signals weekly; link the few promoted items below.

## Attention

Obsidian 1.14+: enable the core Bases plugin to review promoted notes below. Move a card to change its **attention**, then open the note to review its rationale and lifecycle status.

![[4. Management/Management.base#Attention]]

## Review dates

![[4. Management/Management.base#Review dates]]

The Dataview views below remain available for comparison. Daily Record bullets continue to feed the LifeOS weekly view.

## Open decisions

```dataview
TABLE needed_by AS "Needed by"
FROM "4. Management/Decisions"
WHERE type = "decision" AND status = "open"
SORT needed_by ASC
```

## Open risks

```dataview
TABLE review_on AS "Review"
FROM "4. Management/Risks"
WHERE type = "risk" AND status != "closed"
SORT review_on ASC
```

## Systemic problems

```dataview
TABLE status, review_on AS "Review"
FROM "4. Management/Systemic Problems"
WHERE type = "systemic-problem" AND status != "resolved"
SORT review_on ASC
```

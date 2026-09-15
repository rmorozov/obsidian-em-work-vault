# Management cockpit

Open today's LifeOS daily note and capture safe observations under **Daily Record**. Review the signals weekly; link the few promoted items below.

## Attention

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

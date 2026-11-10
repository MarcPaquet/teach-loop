# Friction log

One line per session, written by `debrief`. It records how sessions went, so the skills change on counts instead of
impressions. This is the single home of the line format; field definitions are in `.claude/skills/debrief/metrics.md`.

Line format:

```
date · skill · [[note]] · units done/planned · first-try correct a/b · sure-wrong n · help max H<n> · re n · recall since last a/b · pace · remark
```

## Change on trial

*None. At most one change at a time: one edit to one skill file, agreed by the learner, with its start date, the metric
expected to move, and the replaced text. Judged after three sessions against the three before.*

## Log

## Trial history

*Newest last. Outcomes: `YYYY-MM-DD to YYYY-MM-DD · file · change · metric: name, before to after · kept|reverted`.
Declined proposals: `YYYY-MM-DD · declined: <change in a few words>`; `debrief` reads these before proposing, so a
declined change is not proposed again within three sessions.*

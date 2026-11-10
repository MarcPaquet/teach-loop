# Metrics

How `debrief` counts a session, and how it judges a trial. Everything here is derived from files, except the two
fixed questions.

## Source of counts

A *scored item* is one result line (`**Result:** ...`, format in `../teacher/conventions.md`) in the session's note,
probe and warm-up items included. Parse each into its five fields: result, confidence, help rung, miss type, `re`.

Find them with `grep -n "Result:" <note>`. A scored item without a result line is not counted; Resume reports it.

## Fields of the log line

| Field | Definition |
|---|---|
| `date` | Today, `YYYY-MM-DD`. |
| `skill` | `teacher` or `practice`. |
| `[[note]]` | Link to the session note without extension, e.g. `[[subjects/databases/null-logic]]`. |
| `units done/planned` | Lesson: ticked plan boxes over total boxes. Practice: `-`. |
| `first-try correct a/b` | `b` scored items; `a` of them with result `correct` and help `H0` or `H1` (unaided). |
| `sure-wrong n` | Items with confidence `sure` and result `partial` or `missed`. |
| `help max H<n>` | The highest rung used on any scored item, e.g. `H3`. `H0` if none. |
| `re n` | Sum of the `re` fields. |
| `recall since last a/b` | See below. Practice lines write `-`. |
| `pace` | The learner's answer to question 1: `slow`, `right` or `fast`. |
| `remark` | The learner's answer to question 2, shortened without changing its meaning. |

An item answered `correct` at `H2` counts in `b` but not in `a`; the figure `a/b` is therefore a measure of
unaided performance, not of eventual success.

## Recall since last

Evidence that earlier teaching held, taken from practice notes rather than from the session itself.

1. Find the date of the previous log line. Take every practice note whose `created` date is after it.
2. `b` is the number of scored items in those notes; `a` is those with result `correct` and help `H0` or `H1`.
3. If there is no earlier log line, or no practice note since, write `-`.

This is the only field that looks outside the session. Watch it more closely than the others: a lesson that felt
smooth and a falling `recall since last` mean the lessons are not sticking.

## Reading the numbers

- One session is a single sample of a few items. Report it; do not call it a trend.
- `sure-wrong` is the most informative field. It marks wrong models the learner is confident in.
- `re` growing while `first-try correct` stays flat points to explanations that are not landing.
- `pace` and `remark` are the learner's report and inputs to a trial's proposal. `remark` is never a trial metric;
  `pace` may be one.

## Which metric a trial may name

| Friction seen in the log | Metric to name | Direction |
|---|---|---|
| Items often missed at first try | first-try correct a/b | up |
| Confident wrong answers | sure-wrong n | down |
| Explanations repeated | re n | down |
| Recall weak after lessons | recall since last a/b | up |
| Learner reports `slow` or `fast` | pace | towards `right` |
| Learner needs `H3` or `H4` often | help max | down |

A trial names exactly one.

## Judging a trial

Use the three logged sessions after the start date (the *after* set) and the three immediately before (the *before*
set), restricted to the same `skill` as the trial's file where the file belongs to one skill.

1. For count fields, convert to a rate over the pooled items of each set (for `a/b`, sum `a` over sum `b`; for
   `sure-wrong` and `re`, divide by pooled `b`). For `help max`, use the highest rung in each set. For `pace`, count
   the sessions answered `right`.
2. Write the before and after values side by side in the trial entry.
3. The metric counts as moved when it changes in the expected direction by at least 0.1 on a rate, or by one rung or
   one session for the others. Smaller differences are noise at this sample size.
4. Check one guard: no other rate got worse by more than 0.1. If one did, say which.
5. Present the figures and the guard to the learner with the three options (kept, reverted, extended). The figures
   inform the decision; the learner makes it.

With fewer than three sessions on either side, the judgement is "not enough data": the trial may be extended once.

## Trial history entry

Append under `## Trial history`:

```
YYYY-MM-DD to YYYY-MM-DD · <file> · <the change in one line> · metric: <name>, <before> to <after> · <kept|reverted>
```

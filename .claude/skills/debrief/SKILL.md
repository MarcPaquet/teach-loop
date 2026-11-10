---
name: debrief
description: Closes a teacher or practice session. Checks that the vault can be resumed, measures the session from its result lines and two fixed questions, appends a line to friction-log.md, and proposes at most one agreed change to a skill file. Use when the learner says "debrief" or accepts the one-line offer `teacher` or `practice` makes at the end of a session. Do not use mid-session, to teach (teacher), to retest (practice), or to summarise the learner's progress on request.
---

# debrief

Four steps: **Resume**, **Measure**, **Log**, **Trial**. It runs once per teacher or practice session, after the session's
last note edit. It edits vault files to make them consistent, and edits a skill file only through a trial the learner
has agreed to.

Read first: `../teacher/conventions.md` (result line, callouts, levels, queue formats) and `metrics.md` in this folder
(how to count, how to judge a trial). Do not restate either.

## When to run

- The learner says "debrief", or accepts the one-line offer `teacher` or `practice` makes at the end of a session.
- Run it for one session at a time: the lesson or practice note touched last, or the one the learner names. If two
  notes were touched in one sitting, close each in turn.
- Never run it unprompted in the middle of a session.

## Tone

Plain and dry, as in `teacher`. The measures are counts; report them as counts. Do not interpret one session as a trend.

## 1. Resume

Goal: the next session can start from the files alone. Check, and fix what is mechanical; ask about what is not.

**Lesson note**

- `status` and `next` agree with the plan list. No plan agreed yet (no "Agreed <date>" line above the plan list) means
  `probing` with `next: probe`. A plan agreed with no unit started means `planned` with `next: unit 1`. Some boxes
  ticked means `building` and `next: unit <n>` for the first unticked unit. All boxes ticked means `sealed` and
  `next: done`.
- Plan changes are callouts, and replaced plan lines are struck through, not deleted.
- Every `[!question]` callout (probe, check, problem or warm-up) has an `[!example]` attempt and a verdict ending in a result line (probe items: in
  the *Probe results* block), or is the learner's
  unanswered last item (then `next: pending <item>`). A verdict with no result line, or one not in the standard shape, is reported to the learner and fixed only from what the note already shows.
- A key entry exists in `.keys/lessons/<subject>/<topic>.md` for every item in the note.
- The note appears under *Subjects* in `index.md` and under *Lessons* on its track page, if it has one.
- If sealed: one queue row per completed unit (a unit taught again shares the row of the original), `Source` links
  that resolve to a heading in the note.

**Practice note**

- `items` equals the number of result lines in the note (a two-idea problem has two); the key file exists with one key entry per result line (per item).
- Each problem's queue row was updated; `Close` lists the changes.

**Vault**

- `levels.md`: each *Current* row's `Level` equals the target of its newest History line (`added at L0` counts as
  `L0`); every other History line links to evidence that exists, with the heading present.
- `.keys/queue.md` has the header from `../teacher/conventions.md`, valid `State` values, numeric `Interval`, dates in
  `YYYY-MM-DD`.

Fix typos in structure (a missing `next`, an unticked box for a completed unit). Do not change what the learner
answered, a verdict, or a level. If a level and its evidence disagree, report it and ask.

## 2. Measure

Compute the counts in `metrics.md` from the session note's result lines and from practice notes since the previous log
line. Then ask the learner two fixed questions, one at a time, and record the answers as given:

1. "Was the pace slow, right, or fast?"
2. "What was the least clear point of the session?"

Do not add other questions, and do not offer the counts before the learner has answered.

## 3. Log

Append one line under `## Log` in `friction-log.md`, newest at the bottom, in the line format given at the top of that
file (fields in `metrics.md`). `remark` is the learner's answer to the second question, in a few words. Show the line to the learner.

## 4. Trial

At most one change is on trial at a time. A trial is one edit to one skill file, agreed by the learner, to move one
named metric.

**If a trial is running** (*Change on trial* is not "None"): count the log lines since its start date (or since its `extended:` date, if it has one). With fewer than
three, say so and continue to the end. With three or more, judge it by `metrics.md`: compare the three sessions after
the start with the three before. Offer the learner three outcomes:

- **Kept.** The edit stays; move the entry to *Trial history*.
- **Reverted.** Restore the replaced text recorded in the entry; move the entry to *Trial history*.
- **Extended.** Allowed once, for three more sessions. The entry stays under *Change on trial* with an added line
  `extended: YYYY-MM-DD`, and its three-session count restarts from that date. The second judgement must be kept or
  reverted.

Write the outcome only after the learner chooses.

**If none is running:** propose a change only when the log shows a pattern, such as the same metric poor in two of the
last three lines, or the same remark twice. Otherwise say "No trial proposed." and stop. A proposal states:

1. The evidence (the log lines).
2. The edit: file path, the exact old text and the exact new text.
3. The metric expected to move, and in which direction.

If the learner agrees, make the edit, then record under *Change on trial*:

```
Started YYYY-MM-DD · file: <path> · metric: <name>, expected <direction>
Replaced text: <the old text, verbatim>
New text: <the new text, verbatim>
Judge after: three logged sessions
```

If the learner declines, append one line under *Trial history* in `friction-log.md`:
`YYYY-MM-DD · declined: <change in a few words>`. Before proposing, read the `declined:` lines: do not propose the same
change again while fewer than three log lines have been added since that date.

## Rules

- Never edit a skill file without the learner's agreement in this conversation.
- Never run two trials at once, and never change a second file to "support" the first.
- A trial that touches `../teacher/conventions.md` is a trial on a shared format; say so, since it changes all three skills.
- Judge on the counts in `metrics.md`. Your impression of how the sessions went is not a metric.

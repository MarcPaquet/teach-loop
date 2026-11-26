---
name: debrief
description: Minimal end-of-session close for this vault: checks saved state, logs one friction line, proposes at most one small skill change. Use when the learner says "debrief" or closes a lesson, practice or explore session.
---

# Debrief

Measure how the session went. Edit as little as possible.

## 1. Check the state

Fix only what's missing:

- The lesson or practice note has `status`, `updated` and `next`. For an explore session: the trail and each explore note it touched.
- If a level moved in `baseline.md`, the matching skill note in `skills/` has the same level. Never move a level without a check that showed it.
- If the session taught a skill, its lesson is in that skill note's `lessons`.

## 2. Log one line

Add it under **Log** in `friction-log.md`, even for a smooth session, so a trial has a before and after:

`date · lesson + step · N loops on what · what unlocked it · pace: ok / too hard`

A loop is one more explanation after a miss on the same idea. The session that taught is anchored on its own moves, so the line comes from two other sources, not from rereading the session:

- **The learner, first:** before reading anything, ask them one question for the pace and what unlocked it. Write their words as given.
- **Loops, from the note only:** dispatch a subagent on a smaller model (Sonnet, say) that reads only the sections of the lesson, practice or explore notes dated today and returns one line, `N loops on what`. Give it the loop definition above, and not the transcript or your own read.

Write the line from the two. Where they differ from your own read, theirs wins.

## 3. Look for a pattern

Propose only if one of these is true, and propose one thing:

- **The same friction appears twice and no change is on trial:** propose a change of one or two lines to `teacher` or `practice`. Quote the log lines and say what should improve.
- **Repeated "too hard" on one skill:** this points to a missing prerequisite. Propose a review in the plan, not a skill change.
- **The change on trial has three or more sessions:** show the log before and after, and propose keeping or reverting it.

Then stop. If the learner approves a skill change, apply it, record it under **Change on trial**, and commit it alone with a message starting `Structure:`, when they say to commit.

## 4. Report

Say what's uncommitted. Never commit on your own.

## Never

- Edit a skill, rule, or the graph's structure without approval.
- Run more than one trial at a time.
- Write a feedback memory from friction.
- Add other wrap-up jobs here.

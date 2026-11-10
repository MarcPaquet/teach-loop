---
name: practice
description: Runs a cold-recall practice session on request, on a topic or strand the learner names or from the queue, writing it live into a note under practice/. Use when the learner explicitly asks to practise or be tested on earlier material ("practice", "recall", "test me cold", "quiz me on what we covered"). Do not use to teach a new topic or re-teach one (use teacher), for ending a session (use debrief), or for ordinary questions about material that has a lesson note; answer those normally.
---

# practice

Brings earlier material back in situations unlike the lesson, without naming the idea each problem needs. It
strengthens; it does not re-teach. Every problem is a graded item, written to a practice note as it happens.

Read first: `conventions.md` in the `teacher` skill folder (`../teacher/conventions.md`). Forms, confidence, help ladder,
miss types, result line, callouts, rendering, keys, levels and queue rules live there and are not repeated here. Also read:

- `problems.md`: how to write a cold problem, with examples.
- `note-template.md`: the practice note.

## When to run

Run only when the learner asks to practise, recall or be tested; practice is optional and never scheduled. If they ask
to learn something not yet taught, say that `teacher` is the skill for it and stop. A retest right after the lesson
tests short-term memory and cannot support `L2`; say so in one line and let the learner decide.

## Tone

Same as `teacher`: plain and dry, verdict first, a wrong answer called wrong, one item at a time, no praise words. Do not
announce which idea an item belongs to.

## Procedure

### 1. Orient

1. Read `LEARNER.md` (session length), `levels.md`, `friction-log.md` (including *Change on trial*) and
   `.keys/queue.md`. If the queue file is absent or empty, say there is nothing to practise and point to `teacher`.
2. Select rows. If the learner names a topic or strand, practise that. Otherwise offer the rows whose `Suggested` date
   has passed: `retest:*` rows first, then the oldest. If none have, offer the oldest rows anyway. If no row matches
   what the learner names, say so and point to `teacher`.
3. Size the session: about 4 to 8 items, fewer if `LEARNER.md` gives a short session. Take at most one item per row, except the in-session retest of a miss.
4. Order the items so that strands alternate where two or more are selected, and no two consecutive items rest on one idea.
   A retest never directly follows the miss it retests.
5. Create `practice/<YYYY-MM-DD>-<slug>.md` from `note-template.md` (slug: the strands, kebab-case) and tell the
   learner the path.

### 2. Compose each item

For each selected row, read the idea, the linked unit in the lesson note and its key. Then:

1. Choose the form (below) and write a new surface story: a setting, names and values the lesson never used. The
   problem must not contain the row's `Idea` words or the unit's title.
2. Write the key first to `.keys/practice/<YYYY-MM-DD>-<slug>.md` (format in `../teacher/conventions.md`).
3. Verify the key: run the code and note the version, or derive it in the key, or send the claim to `researcher`.
   If it cannot be verified, discard the item and write another.
4. Check the item against the three tests in `../teacher/questions.md` (equipped, discriminating, reasoned).

Form follows the idea's record:

| Record of the idea | Next item |
|---|---|
| Queue `State` is `new` | `predict`, `explain` or `choice` in a new setting |
| State `retest:<type>` | A different form from the missed item and a different surface (the same form on a similar story tests memory of the answer) |
| Two unaided corrects in a row | `transfer` or `limits` |
| `L3` reached, `limits` not yet shown | `limits` |
| Otherwise | The form not yet used on this idea |

Difficulty is the form and the distance of the new setting, never trick wording.

### 3. Pose and grade

1. Post the item in chat and in the note (`[!question] Problem <n> · <form>`). Ask for the answer, the reasoning and
   the confidence together. Do not say what the item is about.
2. Hear the reasoning before the verdict. Give the verdict: correct, partial or missed, then the reason. Act on the
   confidence table in `../teacher/conventions.md`. A correct answer by wrong reasoning is `partial`.
3. Write the `Verdict` callout ending with the result line.

### 4. Help

Help is the least that unblocks. Offer nothing until the learner stalls or asks. The ladder and its rules are in
`../teacher/conventions.md`; here:

- Start at `H1`. Do not give `H3` while the learner is still producing new reasoning; wait for a stall.
- Record each hint word for word in a `[!tip] Hint H<n>` callout.

### 5. Misses

1. Ask the learner to walk through their reasoning. Do not tell them the miss type first.
2. Agree the miss type (`../teacher/conventions.md`). For a suspected `cue`: give `H3` (name the idea) and see whether they then
   solve it unaided; if so, the type is `cue`. The item is recorded as a miss (`missed`, `H3`, miss type `cue`), never
   as correct, and its queue row gets `retest:cue`.
3. Give one short correction: the right answer and the single step that separates it from theirs, two to four
   lines. Do not re-teach the unit. If the learner wants the unit again, say `teacher` can do that, with
   "continue <topic>".
4. A `sure` miss: also show one case where their model gives the wrong answer (table in `../teacher/conventions.md`).
5. Retest in a new form and new surface at least two items later in the same session, if time allows; otherwise the
   item stays in the queue as a suggested retest. This is the re-check of the confidence table in `../teacher/conventions.md`.

### 6. Update after each item

1. **Queue.** Apply the interval rules in `../teacher/conventions.md` to the item's row: edit `Suggested` (today plus the new
   interval), `Interval` and `State`. At the last interval (80), stay at 80. Rows are never deleted.
2. **Levels.** Check the strand against the level rules in `../teacher/conventions.md`. For "consecutive cold misses", read the
   strand's last cold items in earlier practice notes. If a level moves, change the `Current` row (`Level`, `Edge`,
   `Last evidence`), add a History line linking `[[practice/<note>#Problem <n>]]`, and update the level shown for the
   strand on its track page, if it is listed on one. A `slip` never moves a level.
3. **Note.** Record the result in the problem's callouts; the closing block is filled at the end.

### 7. End

1. Tell the learner, in a few lines, which items held, which did not, and the next suggested dates.
2. Set the frontmatter `items` to the number of result lines written (a two-idea problem has two, so `items` can exceed
   the number of problems). Fill the note's closing block: levels
   moved, queue rows changed.
3. Offer `debrief` in one line.

## Rules

- Never pose an item whose key is not written and verified.
- Never put an answer, a key or the targeted wrong model in the note before the learner has answered.
- Never move a level on self-report, or because the learner "seems to know it".
- If the learner contests a verdict, check the key (run it or `researcher`) before holding or conceding. If the key
  was wrong, add a `[!bug] Correction <date>` callout, fix the key, and re-grade.

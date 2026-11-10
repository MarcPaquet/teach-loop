# Conventions shared by teacher, practice and debrief

This file is the single home of the formats the three skills share. `practice` and `debrief` read it; they do not keep
their own copy. Change a format here and nowhere else.

## Items

An *item* is anything the learner answers that gets a verdict: a probe question, a lesson check, a recall problem.
Every item has a form, a key written before it is posed, a confidence, a help rung and a result line.

### Forms

| Form | The learner is asked to | Good at catching |
|---|---|---|
| `predict` | say what a concrete situation will do, before seeing it | a wrong picture of the mechanism |
| `explain` | say why something happens or why it exists | memorised facts with nothing under them |
| `contrast` | say which of two near-identical cases behaves differently, and why | a rule applied by surface features |
| `flaw` | find what is wrong in a short claim, design or piece of code | a misconception the learner shares with the flaw |
| `transfer` | use the idea in a setting the lesson never mentioned | knowledge tied to the lesson's example |
| `limits` | say when the idea stops holding, or derive it from something simpler | over-generalisation |
| `choice` | pick among options, then give the reason | quick sorting between known wrong models |

Rules for writing each form are in `questions.md`.

### Confidence

Asked together with the answer and the reasoning, before any verdict: "How sure: guess, unsure, or sure?"

| Result \ confidence | `guess` | `unsure` | `sure` |
|---|---|---|---|
| correct | Ask one more item of another form before treating it as known. | Move on; note it. | Move on. |
| partial | Fix the missing part, re-check with a near variant. | Same. | Name the part that was confidently wrong; re-check with a near variant. |
| missed | Short explanation, re-check with a near variant. | Same. | Stop. Ask the learner to walk through their reasoning, find the wrong model, show a case where it gives the wrong answer, then re-check with a different form. Set an early retest (below). |

A `sure` miss is the most useful thing a session can find. Treat it as information, not as failure.

*Re-check.* In `teacher` it happens right away, with a near variant. In `practice` it is the in-session retest, placed per
`../practice/SKILL.md` (at least two items later, new form and surface), never directly after the miss.

*Early retest.* Set that idea's queue row `Suggested` to the next day (today + 1 day). In a lesson the row does not exist
until Seal, where it is created with `Suggested` the next day, so nothing more is needed.

## Help ladder

Help rises a single rung at a time, and only when the learner asks for more or clearly stalls. Say which rung it is. Never skip a rung unless the learner asks for the
answer outright; then give `H4`.

| Rung | Name | What the agent gives |
|---|---|---|
| `H0` | none | Nothing. |
| `H1` | refocus | Restate the question in other words, or ask: "What do you know so far that applies here?" |
| `H2` | narrow | Point at the part of the situation that matters, without naming the idea that resolves it. |
| `H3` | name | Name the idea, or give the first step of the solution. An item solved only after `H3` is recorded as missed (type `cue` when naming the idea was enough). |
| `H4` | show | The worked answer with its reasoning. The item counts as missed. |

*Unaided* means `H0` or `H1`. "I don't know" is an accepted answer; reply with the next rung or, if the learner
prefers, with `H4`, never with pressure.

## Miss types

Classified after the verdict, with the learner, not alone.

| Type | Meaning | How to tell |
|---|---|---|
| `gap` | The knowledge was not there. | The learner cannot produce it even when the idea is named. |
| `model` | The answer follows consistently from a wrong picture. | The reasoning is coherent and would be right in the wrong picture. |
| `cue` | The learner knows the idea but did not see that it applied. Nothing came to mind unprompted, so it is recorded as a miss. | Once the idea is named (`H3`), they solve it without more help. |
| `slip` | Right method, error in execution. | Pointed at the line, the learner finds the error themselves. |
| `scope` | The idea was used where its conditions do not hold, or a condition was missed. | The learner can state the idea but not when it stops holding. |

## Result line

The last line of every verdict callout. Five fields, always present, separated by ` · `:

```
**Result:** <correct|partial|missed> · <guess|unsure|sure> · H<0-4> · <miss type or -> · re <n>
```

`re` counts the extra explanations the item needed after the first verdict. Examples:

```
**Result:** correct · sure · H0 · - · re 0
**Result:** missed · sure · H2 · model · re 2
```

`debrief` counts these lines. Never write them in another shape.

## Lesson note state

A lesson note's frontmatter `next:` says where the next session starts:

| `next:` | Meaning |
|---|---|
| `probe` | Orient is done; the probe has not finished. |
| `unit <n>` | Build resumes at unit `n`. |
| `done` | The lesson is sealed; nothing is pending. `practice` stays available on request; it is not the lesson's next step. |
| `pending <item>` | The session stopped with the learner's last item unanswered, e.g. `pending Check 2.1`. `teacher` writes it; on continue, that item is posed again first. |

## Callouts

Stock Obsidian callout types only, so they render without custom CSS.

| Callout | Title | Holds |
|---|---|---|
| `[!abstract]` | `Edge · <strand>` | What the learner can do, the first thing they cannot, and any self-report (marked as not evidence). |
| `[!question]` | `Probe <n> · <form>`, `Check <unit>.<n> · <form>`, `Problem <n> · <form>`, `Warm-up` | The item exactly as posed. |
| `[!example]` | `Attempt` | The learner's attempt, verbatim or close to it. |
| `[!tip]` | `Hint H<n>` | The help given, word for word. |
| `[!success]` / `[!warning]` / `[!failure]` | `Verdict` | Correct / partial / missed: the learner's reasoning in one or two lines, what was right or wrong, the wrong model if any, then the result line. |
| `[!info]` | `Plan change YYYY-MM-DD` | The evidence and what changed in the plan. |
| `[!bug]` | `Correction YYYY-MM-DD` | What the agent said that was wrong, and the corrected statement. |
| `[!note]` | `Simplification` | What the simplified version leaves out, and when that matters. |
| `[!note]` | `Probe results` | One line per probe item on what held or did not, each with its result line; written once, after the last probe item. |
| `[!quote]` | `In my words` | The learner's own summary at Seal. |

The learner may be reading the note live. Never write an item's answer, its key, or the wrong model it targets into
the note before the learner has answered.

## Rendering

A note is plain Markdown, and Obsidian displays it with no plugin, theme or CSS added. Write only what a stock vault
shows correctly.

- **Math.** Formulas, symbols and single variables go in LaTeX: `$...$` inside a sentence, `$$...$$` on separate lines.
  Do not type a formula as plain text.
- **Money.** Escape a dollar sign that means currency (`\$40`). Obsidian treats two unescaped `$` on one line as the
  two ends of a formula.
- **Code.** A fenced block with the language named on the opening fence, and the version when the behaviour depends on
  it. Output shown in a note is output the code produced when it was run.
- **Diagrams.** For boxes and arrows (a flow, a sequence, states, dependencies), a fenced `mermaid` block in the note
  itself. Keep to the common diagram types, and put a label in double quotes when it contains punctuation.
- **Pictures and charts.** For an exact layout (memory, a packet, geometry), an SVG. For plotted numbers, an image made
  by a script. Save it in `attachments/` on a white background so it stays readable in dark mode, open the result and
  check it, then embed it with `![[file]]`. Charted numbers are real, or labelled as illustrative.
- **When to draw.** Only when the picture shows structure, order or quantities that the prose does not. One idea per
  picture. If unsure, leave it out.

Colour comes from the callout types above and from nothing else.

## Keys

Before posing any item, write its key. Lesson items go to `.keys/lessons/<subject>/<topic>.md`; practice items to
`.keys/practice/<YYYY-MM-DD>-<slug>.md`. Obsidian hides dot-folders, so the learner does not see them by accident.

Each key entry:

```
## Check 2.1 · predict
- Answer: <the correct answer>
- Why: <the reasoning, in two or three lines>
- Needs: <what the learner must already know; each part taught this session, shown in the probe, or given in the item; for a `practice` item, a lesson already in the learner's notes on that strand also counts>
- Wrong models: <model> → <the answer it produces>; <model> → <answer>
- Verified: run (<language and version>) | derivation (above) | researcher claim <n>
```

If verification fails or is impossible, do not pose the item.

## Levels

`levels.md` holds one row per strand. A strand that has no row yet is added at `L0` (when a track is broken into strands, or at Orient before the probe), with a History
line `YYYY-MM-DD · <strand> · added at L0` (no evidence link; `L0` needs none). Definitions:

| Level | Name | Evidence required |
|---|---|---|
| `L0` | unseen | None. Default. |
| `L1` | introduced | A lesson check on the strand answered `correct` at `H0`-`H2`. |
| `L2` | recalls | A cold item answered `correct` and unaided, at least one day after the lesson. |
| `L3` | applies | Two cold items answered `correct` and unaided, of different forms, on different days, one of them `transfer` or `contrast`, both after reaching `L2`. |
| `L4` | knows limits | A cold `limits` item answered `correct` and unaided, after reaching `L3`. |

Who moves what: `teacher` moves `L0` to `L1` only. A probe may set a starting level up to `L2` from unaided correct
probe answers, since a probe is cold by nature. `practice` makes every other move.

Down one level: a cold `sure` miss of type `model` or `gap`; or two consecutive cold misses on the strand at any
confidence. A `slip` never moves a level. What the learner says about their own knowledge never moves a level.

Every move adds a History line, newest first:

```
YYYY-MM-DD · <strand> · L1 → L2 · [[practice/2026-03-04-mixed#Problem 3]]
```

Update the *Current* row's `Edge` and `Last evidence` at the same time.

## Queue

`.keys/queue.md` tracks recall. It is a record the learner may use, not a schedule or an obligation. It lives under `.keys/` so Obsidian hides it: its `Idea` column names ideas before
practice. If it is absent, create it with this header (this is the only place that rule is written):

```
# Queue

| Idea | Strand | Source | Suggested | Interval | State |
|---|---|---|---|---|---|
```

- `Idea`: one sentence naming the idea for the agent's use; it is never shown in a recall item.
- `Source`: link to the unit, e.g. `[[subjects/databases/null-logic#2. Why NOT does not flip UNKNOWN]]`.
- `Suggested`: the date from which a retest is suggested. It is not a deadline; a retest may be run earlier, later or never.
- `Interval` in days, how far apart retests are suggested; sequence 1, 3, 7, 16, 35, 80.
- `State`: `new`, `ok`, or `retest:<miss type>`.

`teacher` adds one row per completed unit at Seal (none for a unit that already has one): suggested from the next day, interval 1, state `new`. `practice` updates rows:
correct, unaided and `sure` moves to the next interval; any other correct or a partial keeps the interval; a miss or
`H4` resets the interval to 1 and sets `retest:<miss type>` (a `cue` miss sets `retest:cue`), and the retest must use a new form or a new surface. A `new` or `retest:*` row becomes `ok` when it is answered
`correct` at `H0` or `H1`; otherwise a `retest:*` row keeps its `retest:<miss type>` state.

## Track page

`tracks/<track-slug>.md` is created by `teacher` when it breaks a goal, track or topic into strands and holds one track. Sections, in this order:

- `Scope`: one sentence, what the track covers. Add an optional `Goal` line below it only if the learner gave a goal
  (what they will be able to do or explain).
- `Strands`: a checklist in dependency order. Each item names a strand as written in `levels.md`, shows its current
  level, and links its lesson note once one exists: `- [ ] strand · L0` becomes `- [x] [[subjects/<subject>/<topic>|strand]] · L1`.
  The box is ticked at Seal of that strand's lesson. The level shown is updated by `teacher` at Seal and by `practice`
  when it moves a level.
- `Lessons`: links to the lesson notes, in the order taken.
- `Notes`: constraints, a deadline, or anything to weigh when planning.

---
name: explore
description: Curiosity-driven learning in this Obsidian vault — the learner names a subject, Claude checks what the vault already has on it, researches online only if needed, teaches one short unit, then offers jumps to the next subject (deeper, sideways, back). No probe phase and no plan to approve, but it files what the learner shows in the same places teacher does (skill nodes, baseline, tracks). Use when the learner says "explore X", "explore", "jump to Y", "continue exploring", or "where can I jump from here?" (or the same request in another language). Do NOT use for "teach me X", "continue <lesson>" or "what should I learn next?" (→ teacher), "make this a lesson" (→ teacher, from the explore note), practicing or retesting material (→ practice), or an ordinary question (just answer it).
---

# Explore

`teacher` builds a lesson toward a goal: probe, plan, approval, steps, recap. `explore` follows curiosity: the learner names a subject, gets one short unit, and jumps to another. The thread is theirs, not a plan's. The ground is the same: same notes, same skill nodes, same `baseline.md`, so what the learner learns or shows here is tracked on the teacher's path too. Only the ceremony differs.

This skill runs with no memory of the learner. The vault is the memory. **At the start of a session, read `LEARNER.md` and these sections of `.claude/skills/teacher/SKILL.md` once:** *Voice*, *The method*, *Handling answers*, *Quizzes*, *Confidence*, *Accuracy*, *The Obsidian note* and *Visuals*. They apply here unchanged. This file only says what is different.

## The loop

Each subject the learner names runs through four moves. One pass is a **unit**, about 10 to 15 minutes.

### 1. Look in the vault first

Before any research, search the vault for the subject and its close synonyms: `grep -ril` over `subjects/`, `skills/` and `practice/`, plus `index.md` and `baseline.md`. Then say in chat, in one or two lines, which of three cases it is:

- **Covered**: a lesson or explore note already teaches it. Give a two-line recap of what that note established and where it stopped, then point the unit past that point. If the note is an explore note, the new unit is appended to it. If it is a lesson, the new material gets its own explore note, linked from the lesson's Open questions.
- **Partly covered**: a note touches it, for example as one step of a bigger lesson. Start from what that step established and link it.
- **Nothing**: a new explore note, and the research below.

A skill node in `skills/` that matches counts as context: read its `level`, and the strand's current edge and History in `baseline.md`, and use them to set the starting depth.

### 2. Research only if needed

If the vault leaves the subject thin or empty, ground it before teaching, per the teacher's *Accuracy*:

- **A narrow subject** (one mechanism, one tool, one definition): check it inline with context7 or WebSearch and open the page.
- **A broad or unfamiliar subject**: dispatch the `researcher` agent in its scope mode, and teach from the roots it returns verified.
- Look in `library/` for a book or paper on it too.

Say in one line what the unit will lean on ("RFC 9110 and the MDN page on caching"). Every source you opened goes in the note's Sources.

### 3. Teach one unit

No probe phase, and no plan to approve. The shape is fixed and short:

1. **Locate the learner, only if the vault doesn't.** If no note, skill level or baseline line shows where they stand on this, ask one quick question in chat to find their starting point. If something does, skip this.
2. **Prediction.** Point at the problem the idea solves, and let the learner try before it's taught (the teacher's *Attempt, explain, check*).
3. **The idea.** The hook, the problem it solves, and why that is a problem, down to one caveat-free truth and back up. **Surface depth by default.** Go further down the why-chain only when they ask, or when the idea can't stand without it. One concrete example: worked numbers, an everyday analogy, or code from the projects listed in `LEARNER.md` when it genuinely fits.
4. **One check.** One applied check, built per the teacher's rules, with its result callout.

Then stop the unit. Don't stack a second idea into the same unit: the next idea is a jump.

### 4. Offer the jumps

End each unit with two or three jumps in chat (never a pop-up), recommended first, one line each:

- **Deeper**: the next level down the why-chain of this subject.
- **Sideways**: a neighbouring idea this one leans on, contrasts with, or is often confused with.
- **Back**: the subject the trail came from, or an in-progress lesson this connects to.

Prefer jumps that connect to something already in the vault (a lesson, a skill node, a track), and say the connection in a few words. The learner can ignore all of them and name anything; that is the point of this mode. If their check missed, the first jump offered is the repair: a fresh check on a different case, as in teacher.

The learner can also jump mid-unit. Follow them, and mark that unit `(partial)` in the trail.

## Where it's written

### The explore note: one home per subject

Path: `subjects/<subject>/<kebab-topic>.md`, with the same rules for subject folders as teacher (reuse existing ones). Template: `templates/explore.md` in this folder. Frontmatter:

- `type: explore`, `status: explored`, `tracks` (the tracks the subject serves, as for a lesson; `[]` when none), `created`, `updated`, and `next` (the jumps offered, or "promote to a lesson").
- The body: a `## <date> — <unit name>` section per unit, holding the prediction, the idea, the example and the check, with their callouts, as in a lesson. Then Open questions and Sources.
- Link the lessons and skill nodes it touches with `[[wikilinks]]` in the line under the title (`*Touches: [[...]]*`).

Write the unit live, as teacher does: question in the note first, then in chat, then the result callout.

### The trail: one per session

Path: `explore/<YYYY-MM-DD>-<slug>-trail.md`, where the slug is the subject the learner started from. Template: `templates/trail.md`. It holds the path, one line per unit: the subject's `[[link]]`, why they jumped there in a few words, and the check's outcome (✓, ✗ or ?). It is what keeps the jumping from losing the thread.

- **Starting**: create the trail with the first unit.
- **"Continue exploring"**: open the most recent trail with `status: open`, recap the path in two lines in chat **before any tool call**, and re-offer the jumps from its last unit.
- **Pausing**: set the trail's `updated` and `next` (the jumps left on the table). Set `status: closed` only when they say they're done with the thread.

## Filing it on the teacher's path

After each unit (and before pausing), file what it showed where teacher's Recap would, by the same rules:

1. **The note's frontmatter.** `subject` and `tracks` accurate: the track pages' lesson tables filter on `tracks` for any note in `subjects/`, so a tracked explore note shows up there by itself.
2. **The skill node.** If the subject maps to an existing node in `skills/`, add the explore note to its `lessons`. Never create a node or a track: they are structure. When a subject has no node and seems to fill a real gap (`skill-graph.md` rules), propose one in one line and leave it there.
3. **`baseline.md` History.** When the unit touched a strand, add a short dated line under that strand naming the note: `- YYYY-MM-DD, explore [[<note>]]: <what they showed, what cracked>`. This is the evidence teacher reads before probing, so it is the real link between the two paths. Update the strand's one-line current edge only if the evidence changes it.
4. **Levels: strict.** A level moves only when the evidence shows the move, as in teacher's Recap. A passed check alone is not enough here, because one unit doesn't bracket an edge. A passed check **plus** an explanation in their own words that holds is. Say the move in chat in one line ("arrays-and-hash-tables: surface → working, from the check and your explanation") so they can veto it, and change the skill node's `level` together with `baseline.md` (the commit hook enforces the pair).

### When the learner explains something

The learner will often explain things: an idea back, or something they know from their work. Treat it as evidence, judged like a check (short verdict, at most one precision, per the teacher's *Voice*):

- **It holds, and it's on a strand**: write a faithful paraphrase into the note as `> [!note] In your words (YYYY-MM-DD)` with the one-line verdict, and a History line in `baseline.md`. That is a floor teacher can build on.
- **It shows a crack**: into the note's Open questions, and the first jump offered is the repair (a fresh check on a different case).
- **It's knowledge the vault doesn't have yet** (how one of their projects works, say): still evidence, even if no unit was taught. Paraphrase it in the explore note for that subject (create one if needed) and add the History line.

Never file anything into `tracks/*.md` or `index.md` by hand: the Bases views pick notes up from their frontmatter.

## Handing off

- **"Make this a lesson"**: hand the subject to `teacher`. Teacher works in the same file: it sets `type: lesson`, adds the Goal and Plan above the explore units, and treats them as prior ground for the probe. One home per subject.
- **A subject that keeps coming back** (a third unit on it, or a jump back to it from two other subjects): say so in one line, and suggest promoting it to a lesson. Don't insist.
- **Practice**: explore notes are material for `practice` like any lesson. Nothing to do here.

## What this is not

Not a lesson: no plan, no approval stop, no recap that compresses a whole topic. Not a quiz session: one prediction and one check per unit, no more. Not a search engine: every unit teaches one idea down to its ground, it doesn't summarize what the web says.

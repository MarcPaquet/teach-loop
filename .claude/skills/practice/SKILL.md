---
name: practice
description: Practice sessions for this Obsidian vault — retests what the learner was already taught by posing problems from new situations that never name the idea they call for, so the idea gets recognized and used without the lesson's prompting. Use when the learner asks to practice, drill or retest taught material — "practice <topic>", "drill me on <lesson>", "retest me", "practice session", "what should I practice?" (or the same request in another language) — or brings an outside problem to try against what they were taught. Do NOT use for a new lesson or "continue <topic>" (→ teacher), material no lesson covers yet (→ teacher or explore), a session an add-on in `LEARNER.md` defines (→ teacher), stress-testing a plan or decision (not this skill), or an ordinary question (just answer it).
---

# Practice

Practice tests taught material cold. A session leaves four things in the vault: a practice note with each problem and its result, the hidden keys in `.drills/`, **Retests owed** for what didn't hold, and dated History lines in `baseline.md`. Gaps too big for it go to the lesson's Open questions, for the teacher. What separates it from a lesson's check is the problem itself: it arrives with nothing around it that names the idea (*What a practice problem is*, below).

This skill has no memory of the learner; the vault does. Lesson notes live in `subjects/`, earlier sessions in `practice/`, and the learner's levels in `baseline.md`: read them rather than guess. Read `LEARNER.md` and the teacher's *The learner* once at the start.

## Voice

Same as the teacher's *Voice*, plus: short replies while the learner works; they are solving, not reading.

## What a practice problem is

A **cold** problem: it arrives without the lesson around it, in a setting the lesson never used, and its wording never names the idea it needs. The learner has to see from the situation which idea applies, then use it.

- **The setting is new:** another domain, other names and numbers, and where the idea allows, another tool or language. Nothing echoes the lesson's title, its example, or the wording of the step it comes from.
- **The idea is needed, not recognized.** If the problem can be answered by spotting a term, it's a vocabulary test: rewrite it so the idea is needed to predict, explain or fix something.
- **Difficulty is the form and the distance** of the new setting from the lesson, never tricky wording.
- **A retest changes both form and setting.** The same problem retold tests memory of the answer, not the idea.

Help goes through the H ladder (below). A gap the ladder can't close goes on the note's **For the teacher** list.

## The material

**Never require anything the material didn't give the learner.** A problem that depends on a fact never taught isn't practice; it's a trap.

1. **Lessons the learner names (the usual case).** Read those notes in `subjects/`. What they taught is the material: the ideas in the Recap, each step's caveat-free truths and derived steps, the dependency map. Look in them for targets:
   - each `[!failure]` quiz and each `[!warning] Correction`: the wrong model the learner once held is a ready-made wrong answer for a `contrast` or `choice` problem;
   - the recurring weak spots in that strand's current edge and History in `baseline.md`;
   - premises that many later steps depend on.
2. **No material named** ("what should I practice?"): offer two or three options in chat as a short list (never a pop-up), recommended one first, ranked as follows: retests owed in `practice/` notes, then finished lessons never practiced, then the lessons practiced longest ago.
3. **A topic the learner describes loosely, a file, a PDF in `library/`, or an outside problem.** Find the lessons in `subjects/` that cover it and use them as the material. If none does, say that practice needs taught material and offer `teacher` or `explore`. An outside problem is posed as P1 with the usual key, which names the lessons it draws on; if no lesson covers it, it goes to `teacher`.

Before the first problem, read earlier `practice/` notes on the same lessons (their `lessons:` frontmatter): their **Retests owed** come first.

## The forms

Every problem has one form:

| Form | The learner is asked to | Catches |
|---|---|---|
| `predict` | say what a concrete situation will do, before seeing it | a wrong picture of the mechanism |
| `explain` | say why something happens or exists | facts held with nothing under them |
| `contrast` | say which of two near-identical cases behaves differently, and why | a rule applied by surface features |
| `flaw` | find the one defect in a short claim, design or snippet | a misconception they share with the defect |
| `transfer` | use the idea in a setting the lesson never touched | knowledge tied to the lesson's example |
| `limits` | say when the idea stops holding, or derive it from something simpler | over-generalizing |
| `choice` | pick among three options, then give the reason | sorting between known wrong models |

Writing each one:
- `predict`: ask before the outcome is visible, never after.
- `explain`: ask *why*, not *what*; a good answer names the problem the thing solves.
- `contrast`: the two cases differ in one detail, and only that detail changes the outcome.
- `flaw`: exactly one defect; two make their reasoning unreadable.
- `transfer`: check that the conditions that made the idea hold in the lesson also hold in the new setting. If they don't, it's a `limits` problem: label it so.
- `limits`: accept any correct boundary with its reason; the key lists every boundary you know.
- `choice`: options built by the teacher's option rules (*Quizzes*); the learner gives the reason with their pick, and a right pick with a wrong reason is `partial`.

The form follows the target's record (earlier practice notes plus this session):

| Record | Next problem on it |
|---|---|
| Never practiced | `predict`, `explain` or `choice` |
| A retest owed | a different form from the problem they missed |
| Two solves in a row, both H0–H1 | `transfer` or `limits` |
| At *working* in `baseline.md`, `limits` not yet shown | `limits` |
| Otherwise | a form not yet used on it |

## Building the session

1. **Targets.** Retests owed first, then the material's weakest points, then the targets practiced longest ago.
2. **Size.** From the *Session length* in `LEARNER.md`: for a session of about 30 minutes, 4 to 8 problems. At most one problem per target, plus the retest of a miss from this session.
3. **Order.** Alternate strands when there are two or more. Never two problems in a row on the same idea. A retest comes at least two problems after the miss it retests, never right after it.
4. **Each problem before it's posed:**
   - choose the form, then write a new setting for it;
   - write the hidden key (below), then verify it: run the code and note the version, derive it step by step in the key, or send the claim to `researcher`. A key you can't verify means a discarded problem;
   - pass three tests. **Equipped:** everything needed was taught in the material or is given in the problem. **Discriminating:** at least one plausible wrong model gives a visibly different answer, and no shortcut reaches the answer without the idea. **Reasoned:** the problem asks for the learner's reasoning with their answer, so the verdict can judge the reasoning.
5. **Retests.** Each miss, and each problem solved only after H2, is retested at least two problems later, in a new form and setting. What doesn't fit in the session goes to **Retests owed** in the note.

## One problem: the protocol

**Posing it** (a single turn):
1. Add the hidden key to `.drills/practice-<YYYY-MM-DD>-<slug>.md`. It's a dot-folder, so Obsidian never shows it, and it stays committed so a paused session resumes on the same key. Record: problem id, target (lesson + step), form, setting, the model solution as numbered moves, each wrong model with the answer it gives, the shortcut you ruled out, and how the key was verified.
2. Write the problem into the note: the exact question the learner answers, with numbered sub-questions if it has parts, never an instruction about how to answer. When code is involved, show it the way `LEARNER.md` *How I learn best* says; by default, code where it helps, explained in words. If the learner asks what the question means, rewrite the problem in the note and in chat; that isn't a hint.
3. Ask the same exact problem in chat, end with *"Think out loud; when you commit to an answer, say how sure you are: guess, unsure or sure."*, and end the turn.

The learner replies in chat. Read transcription slips generously (more so when `LEARNER.md` *How I answer* says answers are dictated), and ask when one word could reverse the meaning. A reply with a confidence word (guess, unsure, sure) is the committed answer. A reply that states an answer without one gets a single line back: "Is that your answer?" Anything else is still working.

**Help: the H ladder.** Offer nothing until the learner stalls or asks. Then one rung at a time, and say which rung it is:

| Rung | Name | What you give |
|---|---|---|
| H0 | none | nothing |
| H1 | refocus | the question in other words, or "what do you already know that applies here?" |
| H2 | narrow | the part of the situation that matters, without naming the idea that resolves it |
| H3 | name | the idea, or the first step of the solution. A solve after this counts as a miss (`cue` if naming it was enough) |
| H4 | show | the worked answer with its reasoning. A miss |

- No H3 while they are still producing new reasoning: wait for a real stall.
- Skip straight to H4 only when they ask for the answer outright. "I don't know" is an accepted reply: answer it with the next rung, or with H4 if they prefer, never with pressure.
- Record each hint in the note as `> [!tip] Hint — H<n>` with its exact text.

**The verdict** is one word, correct, partial or missed, and one line in chat on what held and where it broke. Partial means a right answer reached by wrong reasoning, or an incomplete one. After partial or missed the problem stays open, and if they stall, the next H rung is the only help. Their confidence is read with the teacher's *Confidence* table; a `sure` miss also gets a `contrast` problem against the same wrong model later in the session.

Each miss gets a type, taken from their reasoning and from what the hints changed, never by asking them why:

| Type | Meaning | How it shows |
|---|---|---|
| `gap` | The knowledge wasn't there | They can't produce it even once the idea is named |
| `model` | The answer follows consistently from a wrong picture | Their reasoning is coherent, and right inside the wrong picture |
| `cue` | The idea is held but wasn't seen applied | Once it's named (H3), they solve it without more help |
| `slip` | Right method, error in carrying it out | Pointed at the line, they find the error themselves |
| `scope` | The idea used where its conditions don't hold | They can state the idea but not where it stops holding |

**Ending a problem.** A problem ends at a solve, at H4, or when the learner says "skip" or "show me". Add the result callout (format below) with the model solution copied word for word from the hidden key, give a one-line verdict in chat, and end the turn without posing anything new.

**Between problems,** the teacher's pause rule applies (*Quizzes*): one line naming what comes next, then wait for "next". If they ask about the problem that just ended, answer it, then wait again.

## The practice note: `practice/<YYYY-MM-DD>-<slug>.md`

One note per session, from `templates/practice.md`. The slug names the material (`<topic>`, `<topic>-and-<topic>`). Chat is for the working; the note is the record the learner can re-test on later.

- **Frontmatter:** `type: practice`, `lessons` (wikilinks to the lesson notes practiced), `tracks` (union of those lessons' tracks), `status` (`in-progress` / `done`), `created`, `updated`, `retests_owed` (a count), `next`.
- **Before the learner answers, the note shows only the problem and the hints.** No target, no form, nothing that names the idea.
- **Result callout:**

  | Outcome | Callout |
  |---|---|
  | Solved at H0–H1 | `> [!success] Solved ✓` |
  | Solved after H2 | `> [!warning] Solved with hints (H2)` |
  | Solved after H3 or H4 | `> [!failure] Missed (H<n>) — retest owed` |
  | The learner ended it | `> [!info] Surrendered — retest owed` (blue: an honest stop isn't a wrong answer) |

  Body, each line starting with `> `: `Your answer: <faithful paraphrase of their final reasoning>` · `Confidence: <guess|unsure|sure>` (only if they gave one) · `Verdict: <correct|partial|missed>` · `Target: [[<lesson>]] step <n> · Form: <form>` · `Miss: <type — one line>` (only if any) · a blank `>` line · `**Model solution**` and the committed moves.
- **Retests owed:** a checklist, one line per problem not solved at H0–H1: `- [ ] P2 — <target in plain words> (new form, new setting)`. Tick it with the problem that retested it: `- [x] P2 — … → retested as P6 ✓`. A later session ticks owed items from earlier notes the same way.
- **Debrief** (end of session): what was solved unaided, what needed which rung, misses by type, and a **For the teacher** list (gaps too big for practice).

## After the session

- Set the note's `status`, `updated`, `retests_owed` and `next`.
- **`baseline.md`:** for each target with a clear result, update the strand's one-line current edge if it changed, and add a short dated line to its History section naming the practice note (e.g. `YYYY-MM-DD, practice [[<practice-note>]]: …`). Move a **Level** only when practice showed what the level means. **Working**: a solve at H0–H1 on a new case. **Solid**: a `limits` problem solved at H0–H1. A `slip` never moves a level; never move one on a single lucky solve, or on confidence alone.
- If practice found an error in a lesson note, add a `> [!warning] Correction (YYYY-MM-DD)` in that lesson, and say so plainly in chat.
- **For the teacher:** append each item to that lesson's **Open questions** yourself, as `- <gap in plain words> (from practice [[<practice-note>]], YYYY-MM-DD)`. The teacher folds these in on the next `continue <lesson>`. If the lesson is `done`, also set its `next` to the gap so "what should I learn next?" sees it.

## Rules

- No problem is posed before its key is written and verified.
- Nothing in the note names the idea, the key or the wrong model before the learner has answered.
- No level moves on self-report, or because they "seem to know it".
- If the learner contests a verdict, check the key (run it or `researcher`) before holding or conceding. If the key was wrong, add a `> [!warning] Correction (YYYY-MM-DD)` under the problem, fix the key and grade again.

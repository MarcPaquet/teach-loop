# Lesson note template

Copy everything below the line into `subjects/<subject>/<topic>.md` at Orient. Replace `<...>`. Sections fill in as
the lesson goes; leave a section heading with `*Not reached yet.*` under it until its phase starts. Formats for
callouts and result lines are in `conventions.md`.

---

```markdown
---
type: lesson
subject: <subject>
topic: <topic>
strand: <strand>
track: "[[<track page>]]"   # omit this line when the lesson belongs to no track
status: probing
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
next: probe
---

# <Topic, as a plain title>

**Goal:** <one sentence: what the learner will be able to explain or do at the end>

## Probe

> [!question] Probe 1 · explain
> <the question as posed>

> [!example] Attempt
> <the learner's answer and reasoning> · confidence: <guess|unsure|sure>

Each probe item records the question and the learner's answer only. Verdicts are written once, after the last probe
item, in the block below.

### Probe results

> [!note] Probe results
> Probe 1 · <one line on what held or did not>
> **Result:** correct · sure · H0 · - · re 0
> Probe 2 · <one line>
> **Result:** <correct|partial|missed> · <guess|unsure|sure> · H<0-4> · <miss type or -> · re <n>

> [!abstract] Edge · <strand>
> Can: <what the answers showed the learner can do>
> Cannot yet: <the first thing they could not do>
> Self-report: <what the learner said about their own knowledge; not evidence>

## Plan

Agreed <YYYY-MM-DD>. Sized for <n> minutes from `LEARNER.md`.

- [ ] 1. <unit title>: <the why-question this unit answers> · check: <form>
- [ ] 2. <unit title>: <why-question> · check: <form>
- [ ] 3. <unit title>: <why-question> · check: <form>

## Units

### 1. <unit title>

> [!example] Attempt
> **Problem posed:** <the problem the idea solves, as given to the learner>
> **Learner:** <their attempt>

<Explanation: the problem, the mechanism, the consequence, the limits. Prose, short paragraphs, one concrete example.
Code blocks state language and version when behaviour depends on them.>

> [!note] Simplification
> <what this explanation leaves out, and when that matters>

> [!question] Check 1.1 · predict
> <the item as posed>

> [!example] Attempt
> <answer, reasoning> · confidence: <guess|unsure|sure>

> [!tip] Hint H1
> <the help given, word for word; omit if none>

> [!failure] Verdict
> Reasoning heard: <one or two lines>
> What was wrong: <plainly>. Wrong model: <name>.
> **Result:** missed · sure · H1 · model · re 1

### 2. <unit title>

*Not reached yet.*

## Seal

> [!quote] In my words
> <the learner's summary, verbatim>

Corrections to the summary: <each error, stated plainly, or "none">

Level moved: <strand L0 → L1, or "none">. Queue rows added: <n>.

## Sources

Claims checked by `researcher` before they were taught.

| # | Claim | Verdict | Fails when | Source |
|---|---|---|---|---|
| 1 | <claim> | <holds, holds-if, wrong or unverified> | <conditions> | <URL> |
```

---

## Placement rules

- A resumed session adds `## Resume <YYYY-MM-DD>` directly above the unit being resumed, holding the warm-up item (`> [!question] Warm-up`, attempt and verdict as for any other item).
- A `[!info] Plan change <YYYY-MM-DD>` callout goes directly under the plan list. Changed plan lines are struck
  through with `~~...~~` and the new line added below them.
- A `[!bug] Correction <YYYY-MM-DD>` callout goes at the place the wrong statement was made; the wrong statement is
  struck through, not deleted.
- Attachments (pictures, charts) go in `attachments/` and are embedded with `![[file.png]]`. Rules for math, code,
  diagrams and pictures are in `conventions.md`, Rendering.

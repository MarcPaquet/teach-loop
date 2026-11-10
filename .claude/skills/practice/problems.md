# Writing recall problems

How to turn a queue row into a cold problem. Forms, confidence and the result line are in
`../teacher/conventions.md`; the three tests (equipped, discriminating, reasoned) and the rules for each form are in
`../teacher/questions.md`. This file covers what is different when the learner has not seen the idea today.

## What "cold" means here

- The setting is new: different domain, names, numbers and, where the idea allows, a different language or tool.
- Nothing in the wording echoes the lesson's title, the queue's `Idea` sentence or the lesson's own example.

If the idea can only be recognised by its name, the problem is a vocabulary test. Rewrite it so the idea is needed to
predict or fix something.

## From idea to problem

1. Restate the idea as a mechanism: what causes what.
2. List where the same mechanism appears outside the lesson's example. Pick one the learner has not met.
3. List the two or three wrong pictures (`../teacher/questions.md`, "Finding the wrong models") and check that the new setting
   separates them from the correct one.
4. Write the story, then the question, then the key. Verify the key before posing.

Naming leaks to remove:

| Leaks | Cold |
|---|---|
| "Using what you know about default argument evaluation, what prints?" | "Two log lines are written one second apart. What timestamps do they carry?" with the code below |
| "Why would a partial index help here?" | "This query is slow on a 40-million-row table although 99% of rows are irrelevant to it. What would you change, and why?" |

## Examples

Each is a problem, then its key. The idea is in the key only.

**`flaw`, a transfer of "a default value is evaluated once, at definition".**

> This helper is meant to stamp each message with the time it was written:
>
> ```python
> from datetime import datetime
> import time
>
> def log(msg, stamp=datetime.now()):
>     print(stamp.isoformat(timespec="seconds"), msg)
>
> log("start")
> time.sleep(2)
> log("done")
> ```
> What do the two lines show, and what is wrong with the helper?

Key: both lines show the same time, the moment the `def` statement ran, because the default expression is evaluated
once at definition, not per call. Fix: default to `None` and call `datetime.now()` inside the function. Wrong models:
"defaults are re-evaluated on each call" (answers: two times two seconds apart); "the time is when the module is
imported, so it is the same only if imported late" (partly right on cause, wrong on the fix). Verified: run (Python
3.12). Note this is the same mechanism as a mutable default, in a setting where nothing is mutated.

**`contrast`, a transfer of "not every decimal fraction has an exact binary representation".**

> In Python, which of these prints `True`, and which prints `False`? Say why they differ.
> (a) `0.5 + 0.25 == 0.75`  (b) `0.1 + 0.2 == 0.3`

Key: (a) `True`, (b) `False`. Python floats are IEEE 754 binary64. 0.5, 0.25 and 0.75 are sums of powers of two, so
they are stored exactly and the addition is exact. 0.1, 0.2 and 0.3 are not, each is the nearest representable value,
and the rounded sum differs from the rounded 0.3 (it is `0.30000000000000004`). Wrong models: "floats are always
approximate" (answers False, False); "the operator rounds for you" (True, True). Verified: run (Python 3.12).

**`limits`, for "an index on a column speeds up lookups by that column".**

> A table `users` has a B-tree index on `email`. The application runs
> `SELECT * FROM users WHERE lower(email) = 'ana@example.org'` and it is slow. In PostgreSQL, can the index serve this
> query? If not, what would? Then say one other kind of condition on `email` that the same index cannot serve.

Key: no, the index is ordered on `email` values, not on `lower(email)`; the planner cannot use it for a condition on
an expression. An expression index on `lower(email)` can. Another condition the plain index cannot serve: a pattern
with a leading wildcard (`email LIKE '%@example.org'`), since the order gives no starting point. Needs: that a B-tree
index is a sorted structure (in the learner's lesson note on that strand). Wrong models: "an index on a column covers any use of the column"
(answers yes). Verified: official PostgreSQL docs, versioned (`researcher` claim). State the version in the key.

## Two ideas in one problem

A problem may use two ideas only when both are in the queue and both are in the learner's record. Each idea gets its own result
line and is scored as a separate item, so `items` counts result lines, not `### Problem` blocks.

## Common faults

- A story that is the lesson's example with names changed.
- Giving the idea in the question for the sake of fairness. Fairness comes from `Needs` (taught, shown, given in the item, or a lesson already in the learner's notes on that strand), not from naming.
- Two defects in a `flaw` item, which makes the reasoning unreadable.

# Writing items

How to write probe questions, lesson checks and (for `practice`) problems. Forms, confidence and the result line are
defined in `conventions.md`.

## Three tests every item must pass

1. **Equipped.** Everything needed to answer was taught this session, shown in the probe, or is given in the item.
   For a `practice` item, a lesson already in the learner's notes on that strand also counts.
   List it under `Needs` in the key. If a needed fact is missing, teach it first or put it in the item.
2. **Discriminating.** At least one plausible wrong model gives a visibly different answer. Name that model and its
   answer in the key. If every model you can think of gives the same answer, the item tests nothing; rewrite it.
3. **Reasoned.** The learner gives the answer, the reasoning and a confidence before any verdict. A correct answer
   reached by wrong reasoning is `partial`, with the miss type of the reasoning.

## Finding the wrong models

Before writing a check for a unit, list the two or three wrong pictures a reasonable newcomer would hold. Sources:

- What the learner's attempt in this unit assumed.
- The everyday meaning of the term (a "cache" that is always current, a "transaction" that is always isolated).
- A neighbouring idea the learner knows, applied where it does not fit.
- The simplification the lesson used, taken as the whole story.

Then pick a situation where those pictures disagree with the correct one.

## Form by form

**`predict`.** Give a concrete, small situation and ask what happens. Ask before showing the outcome, never after.

> A program calls `write()` on a regular file, the call returns success, and the machine loses power one second
> later. Is the written data guaranteed to be on disk? Explain.

Key: No guarantee. On POSIX systems a successful `write()` means the kernel accepted the data, usually into its page
cache; it reaches stable storage later. Durability needs `fsync()` or `fdatasync()` on the descriptor, or a file
opened with `O_SYNC` / `O_DSYNC` (for a newly created file, the directory entry needs the same), and even then
depends on the storage device honouring cache flushes. Wrong model
"returned means on disk" answers yes.

**`explain`.** Ask why, not what. "Why does a database need a write-ahead log if it already writes the table pages?"
beats "What is a write-ahead log?". A good answer names the problem the thing solves.

**`contrast`.** Two cases that differ in one detail, only one of which changes the outcome. Ask which and why.

> Table `t` has one column `c` and three rows: `'x'`, `'y'`, and NULL. How many rows does each query return?
> (a) `SELECT * FROM t WHERE c <> 'x'` (b) `SELECT * FROM t WHERE NOT (c = 'x')`

Key: one row each (`'y'`). Under standard SQL three-valued logic, `NULL <> 'x'` and `NULL = 'x'` are both UNKNOWN,
`NOT UNKNOWN` is still UNKNOWN, and `WHERE` keeps only rows where the condition is TRUE. Wrong model "NULL is just
another value" answers 2 and 2; wrong model "NOT flips everything" answers 1 and 2. Caveat for the key: engine
behaviour and settings can differ (some engines store an empty string as NULL; some have a setting that changes
`= NULL` comparisons), so name the engine in the item if it matters.

**`flaw`.** Show a short claim, design or snippet with one defect that a specific wrong model would not see. Ask what
is wrong and what would happen. Keep the defect to one; two defects make the reasoning hard to read.

**`transfer`.** Same structure, new setting. If the unit used a web cache, the transfer item might use a DNS
resolver's cached record or a build tool's cached artefact. Do not name the idea. Check the transfer is real: the
conditions that made the idea hold in the lesson must also hold in the new setting, or the item becomes a `limits`
item and must be labelled as one.

**`limits`.** "When does this stop being true?" or "Derive this from what you already know." Accept any correct
boundary with its reason; the key lists all the boundaries you know.

**`choice`.** Use when the wrong models are known and few. Rules, all required:

- Every distractor comes from one named wrong model: what a learner holding it would pick. No filler options.
- Options are parallel: same grammatical form, similar length, same level of detail. The correct one is not the
  longest, most hedged or most technical.
- No absolute words ("always", "never") that act as tells unless they appear in every option.
- The correct option's position varies across items. Occasionally the correct answer is "none of these", and then
  the learner must say what the answer is.
- The learner gives the reason for the choice. A correct letter with a wrong reason is `partial`.

Example:

> ```python
> def add(item, bucket=[]):
>     bucket.append(item)
>     return bucket
>
> a = add(1)
> b = add(2)
> print(a, b, a is b)
> ```
> What does the last line print? Give your reason.
> A. `[1] [2] False`  B. `[1] [1, 2] False`  C. `[1, 2] [1, 2] True`

Key: C. A default value is evaluated once, when the `def` statement runs, so both calls append to the same list
object and both names refer to it. This is Python language semantics, not an implementation detail. A comes from
"defaults are re-created on each call"; B from "the default is shared, but `return` hands back a copy".

## Probe ladders

A probe ladder for one strand is two to four items, ordered from the foundation to the depth the goal needs. Stop at
the first miss or "I don't know"; that rung is the edge. Probe items are `explain` or `predict`, never "have you heard
of X" or "rate yourself". The learner's self-report may be noted, labelled as not evidence.

Example ladder for a strand on SQL NULL handling:

1. `explain`: What does a NULL in a column stand for?
2. `predict`: What does `WHERE c = NULL` return, and why? (Key: no rows; the comparison is UNKNOWN, never TRUE.)
3. `predict`: What does `WHERE NOT (c = NULL)` return, and why? (Key: `c = NULL` is UNKNOWN, `NOT UNKNOWN` is
   UNKNOWN, so no rows.)
4. `explain`: Why can `WHERE x NOT IN (SELECT y FROM u)` return no rows at all, even when some `x` values are absent
   from `u`? (Key: if `u.y` contains a NULL, `x NOT IN (..., NULL)` is never TRUE under standard semantics.)

## Common faults to avoid

- An item answerable by recognising a phrase from the explanation. Change the surface.
- An item the learner could answer by copying a line of the note: it measures reading, not understanding. Reword so
  it needs the mechanism, not the sentence.
- A check that needs a fact never taught. Fails the equipped test.
- Several questions in one item. One item, one answer.
- Trick wording. Difficulty comes from the idea, never from the phrasing.

# Practice note template

Copy everything below the line into `practice/<YYYY-MM-DD>-<slug>.md` at Orient. Replace `<...>`. Add one
`### Problem <n>` block per problem as it is posed; the heading is what `levels.md` History lines link to.
A two-idea problem has one block and two result lines; `items` counts result lines.
Formats for callouts and result lines are in `../teacher/conventions.md`.

---

```markdown
---
type: practice
strands: [<strand>, <strand>]
items: 0
key: .keys/practice/<YYYY-MM-DD>-<slug>.md
created: <YYYY-MM-DD>
---

# Practice <YYYY-MM-DD>

Rows drawn from `.keys/queue.md`: <n> selected, <n> of them retests. Nothing below names the idea an item needs; the
sources are listed at the end.

## Problems

### Problem 1

> [!question] Problem 1 · transfer
> <the problem as posed, with its own context: language, version, values>

> [!example] Attempt
> <the learner's answer and reasoning> · confidence: <guess|unsure|sure>

> [!tip] Hint H3
> <the help given, word for word; omit if none>

> [!failure] Verdict
> Reasoning heard: <one or two lines>
> <what held, what did not; the wrong model if one showed>
> Correction: <two to four lines, only after a miss or partial>
> **Result:** missed · unsure · H3 · cue · re 0

### Problem 2

*Not reached yet.*

## Close

Levels moved: <strand L1 → L2, evidence [[practice/<note>#Problem n]], or "none">.

| Row (source) | Before | After |
|---|---|---|
| [[subjects/<subject>/<topic>#<unit heading>]] | suggested <date>, interval 3, ok | suggested <date>, interval 7, ok |

## Sources

The units these problems came from, shown only here, after every problem has been answered.

| Problem | Unit |
|---|---|
| 1 | [[subjects/<subject>/<topic>#<unit heading>]] |
```

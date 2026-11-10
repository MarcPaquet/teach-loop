# Levels

One row per strand. A level moves only on evidence from a lesson check or a cold item, never on confidence or
self-report. `teacher` moves `L0` to `L1` only (a probe may set a starting level up to `L2`); `practice` makes every
other move.

## Definitions

| Level | Name | Evidence required |
|---|---|---|
| `L0` | unseen | None. Default. |
| `L1` | introduced | A lesson check on the strand answered `correct` at `H0`-`H2`. |
| `L2` | recalls | A cold item `correct` and unaided (`H0` or `H1`), at least one day after the lesson. |
| `L3` | applies | Two cold items `correct` and unaided, of different forms, on different days, one of them `transfer` or `contrast`, both after reaching `L2`. |
| `L4` | knows limits | A cold `limits` item `correct` and unaided, after reaching `L3`. |

Down one level: a cold `sure` miss of type `model` or `gap`, or two consecutive cold misses on the strand. A `slip`
never moves a level. Full rules: `.claude/skills/teacher/conventions.md`.

## Current

| Strand | Level | Edge | Last evidence |
|---|---|---|---|
| | | | |

## History

*Dated entries, newest first, each linking its evidence: `YYYY-MM-DD · strand · L1 → L2 · [[practice/2026-03-04-mixed#Problem 3]]`. A new strand starts with `YYYY-MM-DD · strand · added at L0`, which needs no link.*

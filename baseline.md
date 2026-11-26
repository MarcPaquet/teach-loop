---
type: baseline
started: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
status: in-progress
next: ""
---

# Baseline: where I am

A map of your edges, built from explain-it probes (no scores). The table shows each strand's level and current edge
at a glance; the dated evidence and lesson notes are in [History](#history) at the end.

**Level** tracks progress per strand, by what is observable, not by points:

| Level | Meaning |
|---|---|
| **none** | No working model |
| **surface** | Knows the words and workflow, not the mechanism |
| **working** | Can explain the mechanism and apply it to a new case |
| **solid** | Can derive it from first principles and spot when it breaks |

A level moves up only when a lesson's explain-back or apply-to-a-new-case check shows it, or a practice session does
(working: a solve at H0 to H1 on a new case; solid: a `limits` problem solved at H0 to H1, saying when the idea stops
holding or deriving it from something simpler). An explore session moves a level only on a passed check plus an
explanation in your own words that holds. Confidence alone, self-report, or "seems to know it" never moves a level.
When a lesson or practice note shows something new, the strand's row gets its new level and a one-line current edge,
and its History section gets a short dated line naming the note. The matching skill node in `skills/` takes the same
level.

## Strands

Group strands under a heading per domain or track. Add a row only when a probe or lesson gives it a level.

| Strand | Level | Current edge |
|---|---|---|
| *none yet* | | |

## History

Dated evidence per strand, oldest first. The first line of a strand is the original probe.

*Format: a `###` heading per domain, a `####` heading per strand, then one line per note:*
`- **<YYYY-MM-DD>, <lesson | practice | explore> [[note]]:** what the check showed.`

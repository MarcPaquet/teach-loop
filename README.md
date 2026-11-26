# teach-loop

Four Claude Code skills (`teacher`, `practice`, `explore`, `debrief`) and one subagent (`researcher`) that teach, retest and track a learner inside an Obsidian vault. Every lesson, practice problem and exploration unit is written live into a Markdown note, and levels with their dated evidence live in `baseline.md` and a graph of skill nodes, so the learner's record is a folder of plain files under git. It fits one learner per clone, who fills in `LEARNER.md` and runs Claude Code from the vault folder.

Two meanings of "skill" appear below: the Claude Code skills in `.claude/skills/`, and the skill nodes in `skills/`, the pieces of knowledge a level is tracked on.

## How a session runs

```mermaid
flowchart LR
    S(("You say")) --> G(["a goal"])
    S --> N(["what should I learn next?"])
    S --> T(["teach me X"])
    S --> C(["continue X"])
    S --> X(["explore X"])
    S --> P(["practice X"])
    S --> D(["debrief"])

    G -- teacher --> G1("Map the goal to skills") --> G2("Track of ordered lessons") -- "each lesson" --> G3(["teach me X"])
    N -- teacher --> N1("Lesson suggested from your tracks") --> N2(["teach me X or continue X"])
    T -- teacher --> T1("Probe") --> T2("Plan") --> T3("Teach") --> T4("Recap") --> R1[("Evidence filed")]
    C -- teacher --> C1("Next unchecked step") --> C2("Teach") --> C3("Recap") --> R2[("Evidence filed")]
    X -- explore --> X1("Vault check") --> X2("One unit") --> R3[("Evidence filed")] --> J{"Jump"}
    J -- "deeper, sideways, back" --> J1(["explore X"])
    J -- "make this a lesson" --> J2(["teach me X"])
    P -- practice --> P1("Cold problems on what was taught") --> R4[("Evidence filed")]
    R4 -- "miss: retest owed" --> P2(["practice X"])
    R4 -- "gap too big" --> P3(["continue X"])
    D -- debrief --> D1("One line in the friction log") -- "repeated friction" --> D2("One change proposed")

    classDef say fill:#f6f8fa,stroke:#8c959f,color:#1f2328,stroke-width:1px
    classDef teacher fill:#ddf4ff,stroke:#54aeff,color:#0a3069,stroke-width:1px
    classDef explore fill:#dafbe1,stroke:#4ac26b,color:#0f5323,stroke-width:1px
    classDef practice fill:#fff8c5,stroke:#d4a72c,color:#5c3d00,stroke-width:1px
    classDef debrief fill:#fbefff,stroke:#c297ff,color:#512a97,stroke-width:1px
    classDef record fill:#ffffff,stroke:#57606a,color:#1f2328,stroke-width:1px
    class S,G,N,T,C,X,P,D,G3,N2,J1,J2,P2,P3 say
    class G1,G2,N1,T1,T2,T3,T4,C1,C2,C3 teacher
    class X1,X2,J explore
    class P1 practice
    class D1,D2 debrief
    class R1,R2,R3,R4 record
```

Each branch starts from what the learner says and is labelled and coloured by the skill that takes it. A learning branch ends in evidence filed in `baseline.md` (a dated History line, and a level change when a check showed it), and a grey phrase at the end of a branch is the branch the session continues on. A goal (a job offer, a certification, or a broad goal spanning several skills) is mapped to skill nodes and a track of ordered lessons, and each of those lessons runs as `teach me X`: Probe, Plan, Teach and Recap. In Teach, each plan step is an Attempt (the learner works on the problem before it is taught), an Explain that starts from that attempt, and a Check. `explore` has no plan: it looks in the vault, researches only if needed, teaches one unit, files what the unit showed and offers jumps. `practice` retests a miss in a later problem or session, and sends a gap too big for it to the lesson's open questions, where `continue X` picks it up.

## What each piece does

**teacher** runs on "teach me X", "continue X" or "what should I learn next?". A target (a job offer, a certification, or a broad goal spanning several skills) is first mapped to skill nodes and given a track page; a single topic starts at Probe. Probe creates the lesson note and asks a ladder of 2 to 4 questions per prerequisite strand and stops at the first miss or "I don't know": that rung is the learner's edge. Plan sends the lesson's claims to `researcher`, adds a dependency map (at most 8 nodes) and a step checklist, and teaches nothing until the learner approves. The explanation descends a why-chain (what it is, which problem it removes, why that is a problem, what happens mechanically) until it reaches a statement `researcher` would mark ✅ with no condition, then climbs back one motivated move at a time. Graded questions are quizzes of 3 options plus "4. I don't know", written into the note before they are asked in chat; each wrong option is the pick of one named wrong model, and the options are kept within about 20% of each other's length. The learner adds a confidence word (guess, unsure or sure), and the verdict and confidence together pick the next move: a right guess gets another check of a different kind, a sure miss gets the wrong model named and a counter-case. There is no follow-up "why" question after an answer. When answers contradict the plan, the note gets a dated plan-change callout and existing step numbers never change (an inserted step is `2a`). Recap moves a strand's level in `baseline.md` only when the lesson's checks showed it.

**practice** runs on "practice X" or "what should I practice?" and works only from material the vault already teaches. Each problem is cold: a new setting whose wording never names the idea it needs, in one of seven forms (`predict`, `explain`, `contrast`, `flaw`, `transfer`, `limits`, `choice`), picked from the target's record. Before a problem is posed, its key is written to `.drills/` and verified by running code, a step-by-step derivation or `researcher`; a key that cannot be verified means the problem is discarded. Help comes one rung at a time on the H0 to H4 ladder (none, refocus, narrow, name, show), and a solve after H3 counts as a miss. Each miss gets a type (`gap`, `model`, `cue`, `slip`, `scope`) read from the learner's reasoning and from what the hints changed, never by asking. Misses are retested at least two problems later in a new form and setting, or listed as Retests owed. A level moves to working on a solve at H0 to H1 on a new case, and to solid on a `limits` problem solved at H0 to H1; a `slip` never moves one.

**explore** runs on "explore X" or "jump to Y". It searches the vault first and says whether the subject is covered, partly covered or new, and researches only when the vault is thin (inline for a narrow subject, `researcher` in scope mode for a broad one). A unit is one prediction, one idea taken down to one caveat-free truth, and one check. It ends with two or three jumps: deeper, sideways, or back to where the trail came from. Each session keeps a trail in `explore/`, one line per unit with its check outcome. A unit that touches a strand adds a dated History line to `baseline.md`, and moves a level only on a passed check plus an explanation in the learner's own words. "Make this a lesson" hands the note to `teacher`, which works in the same file.

**debrief** closes a session. It repairs missing resume fields (`status`, `updated`, `next`), asks the learner first, in one question, about the pace and what unlocked a miss, and has a subagent on a smaller model count loops (one more explanation after a miss on the same idea) from the day's note sections only, not from the transcript. It writes one line to `friction-log.md` and proposes at most one change, only when the log shows a repeated pattern, with one trial running at a time. It never commits on its own.

**researcher** is a subagent that checks a list of claims, or scopes a topic by writing the 5 to 10 claims a first lesson would make and marking the roots. It checks vendor documentation first, then specs, RFCs and textbooks, with blogs only as corroboration, and cites only pages it opened. Each claim gets ✅ true, ⚠️ true with caveats, ❌ false or ❔ unverified, with the condition or correction and its source, and the report ends with a count line.

**The structure hook** (`.githooks/commit-msg`, `check_structure.py`) checks staged files on every commit. It blocks a change to a Claude Code skill or agent, the hooks, `CLAUDE.md`, `LEARNER.md`, `addons/`, `skill-graph.md` or `skill-lessons.base`, a skill node added, removed or moved, or a change to `needs`, unless the message starts with `Structure:`. It also checks every skill node's frontmatter (fixed keys, a known level, at most 3 `needs`, at least one track, known needs, lessons and tracks, no cycles) and that note filenames are unique, refuses a level change without `baseline.md` in the same commit, and keeps process changes out of commits that touch lesson, practice or explore notes.

## The vault

| Path | Purpose |
|---|---|
| `LEARNER.md` | Filled in by the learner: who they are, aims, track order, how they learn and answer, session length, languages, projects the teacher may read, things to avoid, add-ons |
| `addons/` | Optional files defining extra session types, each listed in `LEARNER.md` with the phrases that start it |
| `index.md` | Entry point: lessons in progress, tracks in their default order, subjects |
| `baseline.md` | One row per strand with its level (none, surface, working, solid) and current edge, plus dated History |
| `skill-graph.md`, `skills/` | Skill nodes, one note each, with `level`, up to three `needs`, `tracks` and `lessons` |
| `skill-lessons.base` | Obsidian Bases table embedded in each skill node, listing the notes in `subjects/` it links to |
| `tracks/` | Goal pages, `foundations.md` and `example-track.md`; a dated track has `ready_by` and a `## Queue` |
| `subjects/` | Lesson and explore notes, `subjects/<subject>/<topic>.md` |
| `practice/` | One note per practice session |
| `explore/` | One trail per explore session |
| `.drills/` | Hidden answer keys; Obsidian does not show dot-folders |
| `friction-log.md` | One line per session, and the change on trial |
| `CLAUDE.md` | Vault rules Claude Code loads in every session |
| `.githooks/` | The structure hook |

## Setup

1. Clone the repository.
2. Fill in `LEARNER.md`. Empty fields fall back to the defaults listed in `teacher`.
3. Enable the hook: `git config core.hooksPath .githooks` (it needs `python3`).
4. Open the folder as an Obsidian vault, with the Bases core plugin enabled.
5. Run `claude` from the folder, so the project skills load.
6. Say `teach me <topic>`. Later: `continue <topic>`, `explore <subject>`, `practice <topic>`, `debrief`.

`tracks/example-track.md` and `skills/example-domain/example-skill.md` are placeholders. Remove them together, in one commit whose message starts with `Structure:`; the hook blocks removing the track alone, because the skill node still lists it.

`researcher` looks up library documentation through the context7 MCP server first, then the vendor's site.

## Limits

- Written for Claude Code and Obsidian only.
- Quality depends on the model and on fact-checking that can still miss: `researcher` returns ❔ when it cannot confirm a claim, and a source it opened can be wrong.
- Levels move on the model's reading of the evidence. The hook checks that a skill node's level and `baseline.md` change together, not that the evidence exists.
- The hook runs only where `core.hooksPath` is set, and only on commits.
- `.drills/` is hidden from Obsidian's file pane, not from the learner: the keys are plain files in the repository.
- It is not a course and ships no content; the vault starts empty.

## License

MIT. See `LICENSE`.

# Learning vault

This folder is an **Obsidian vault** and a Claude Code project for being taught.

- **Lessons**: the project skill `.claude/skills/teacher/`. It triggers only on explicit requests: "teach me X",
  "continue X", "what should I learn next?".
- **Practice**: the project skill `.claude/skills/practice/` retests material already taught ("practice X", "drill me
  on X"). One note per session in `practice/<YYYY-MM-DD>-<slug>.md`; its hidden answer key goes in `.drills/`.
- **Explore**: the project skill `.claude/skills/explore/` follows curiosity: "explore X" checks the vault, researches
  if needed, teaches one short unit, offers jumps. One note per subject in `subjects/` (`type: explore`), one trail per
  session in `explore/<YYYY-MM-DD>-<slug>-trail.md`. It files evidence on the teacher's path (skill `lessons`, `baseline.md`
  History, levels under the same rules).
- **Session close**: `/debrief`.
- **The learner and add-ons**: `LEARNER.md` holds who you are, your aim, track order, how you learn and answer, session
  length, languages, readable projects and add-on triggers. `addons/` holds the add-on files it lists. The skills under
  `.claude/` are generic and read `LEARNER.md` at the start; fill it in before the first session.
- **Layout**: `subjects/<subject>/<topic>.md` (one home per lesson) · `skills/<domain>/<skill>.md` (the skill graph,
  see `skill-graph.md`; levels mirror `baseline.md`) · `practice/` (practice sessions) · `explore/` (explore trails) ·
  `tracks/*.md` (goal pages, plus `foundations` for gaps) · `baseline.md` (levels per strand) · `index.md` (entry
  point) · `friction-log.md` (one line per session, written by `debrief`) · `attachments/` (images and PDFs embedded
  in notes; chart scripts go in `attachments/_src/`) · `library/` (books and papers as PDFs, gitignored).
- **Structure gate**: propose and stop. Changes to skills, `needs`, rules or skill files need the learner's OK and a
  commit message starting `Structure:`. Enable the check once per clone with `git config core.hooksPath .githooks`;
  `.githooks/commit-msg` then enforces it.
- **Hidden files**: `.drills/` holds practice answer keys and any fact sheets an add-on needs. Obsidian doesn't show
  dot-folders; never link to them from a note.
- **Note types**: `type` in a subject note's frontmatter is `lesson`, `drill`, `lab`, `playbook`, `exam` or `explore`.
- **Memory**: the vault is the memory between sessions; the method lives in the skills, the learner in `LEARNER.md` and
  `addons/`; auto-memory holds only what fits neither. Read `index.md` and the relevant tracks before teaching; resume
  lessons from their frontmatter and checklist.
- **Track lesson lists** are Obsidian Bases views driven by lesson frontmatter (`subject`, `tracks`, `status`): keep
  frontmatter accurate instead of editing lists by hand.
- **Fact-checking**: `.claude/agents/researcher.md`.
- Projects listed in `LEARNER.md` may be **read** for lesson examples, never modified.

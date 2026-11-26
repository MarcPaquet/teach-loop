---
type: skill-graph
---

# Skill graph

Every skill is one note in `skills/<domain>/<skill>.md`, and its `needs` property lists the skills it depends on. Open
the graph view to see it: arrows point from a skill to what it needs. The graph starts empty; the teacher adds nodes
as probes and lessons expose gaps.

## What a node is

A small, levelable piece of knowledge, one note with this frontmatter:

```yaml
type: skill
domain: <domain>          # same as its folder
level: unprobed           # unprobed | none | surface | working | solid
needs: []                 # up to three skills, as "[[skill-name]]"
tracks: [example-track]   # every track that needs it
lessons: []               # lessons that cover it, as "[[lesson-name]]"
```

The body is a title, one line on what the skill is, and a `## Lessons` section embedding `![[skill-lessons.base]]`.
See `skills/example-domain/example-skill.md`.

## Rules

- **A need is strict:** A needs B only if you can't reason about A without B. Related isn't enough, and three needs is
  the limit.
- **A skill can be levelled:** if [[baseline]] couldn't give it a level, it's too big or too vague to be a node.
- **Nodes fill real gaps:** add one when something you want to learn, a target or a lesson shows a gap, not to complete
  a curriculum.
- **Filenames stay unique:** a skill can't share a name with a lesson, so it's `threads-races-locks`, not
  `concurrency`.

## Levels

`level` uses the [[baseline]] scale (none, surface, working, solid), plus `unprobed` for a skill nobody has tested yet.
A skill you've never been tested on is `unprobed`, even if a lesson covered it. [[baseline]] stays the source of truth:
when a level changes there, change the node too. Never move a level without a check that showed it.

## Graph colours

Colour shows level: grey is `unprobed`, red is `none`, orange is `surface`, green is `working`, gold is `solid`. Set
the colour groups in Obsidian's graph view with the search `["level":unprobed]` and so on.

## Lessons on a skill

A skill's `lessons` property lists the lessons that cover it, and the table in the note shows each one's status. A
listed lesson can be `planned`: it means the lesson covers the skill, not that you did it.

## Tracks on a skill

A skill's `tracks` property lists every track that needs it, written like a lesson's (`[track-a, foundations]`). Each
track page shows its skills in a **Skills** table grouped by level, so skills still at `none` or `unprobed` show up
before any lesson exists.

## What to learn next

Start from the target: a skill you want, or the skills in a job offer. Walk back through `needs` to what you already
have. The closest thing to learn is the first skill on that path whose needs are met. Bases can't walk prerequisites,
so ask Claude.

- **Target vs level:** `level` is what you can do now and lives on the skill. A target is what you need now, lives in
  the plan, and can change.
- **Starting mid-path is fine:** a need can stay a black box. Go down a level only when a lesson breaks on it, a target
  asks for that depth, or several skills lean on it.
- **Levels go stale:** do a quick check before building on an older level.

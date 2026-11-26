---
type: track
level: target
---

# Example track

*A placeholder goal track: what you are aiming for and why. Copy this page for a real goal and delete this one.
Mapping a target (see the teacher's `mapping-a-target.md`) writes its plan here.*

## Dated tracks

A track with a deadline (an exam, an interview) adds two things. Its frontmatter gets `ready_by`, a date or `TBD`
while the date is unknown, and the page gets a `## Queue` section. Both are needed; `ready_by` alone does not make a
dated track. While it is active, "continue <track>" means the first unchecked item of its Queue.

```yaml
ready_by: <YYYY-MM-DD>
```

```markdown
## Queue

- [ ] 1. <lesson or review> → [[lesson-name]]
- [ ] 2. <lesson or review>
```

This example track has no date, so it has no Queue.

## Skills

Every skill this track needs, grouped by level. Set by the `tracks` property on each skill.

```base
filters:
  and:
    - file.inFolder("skills")
    - 'tracks.contains("example-track")'
views:
  - type: table
    name: Skills
    groupBy:
      property: note.level
      direction: ASC
    order:
      - file.name
      - domain
      - needs
```

## Lessons

```base
filters:
  and:
    - file.inFolder("subjects")
    - 'tracks.contains("example-track")'
views:
  - type: table
    name: Lessons
    groupBy:
      property: note.status
      direction: ASC
    order:
      - file.name
      - subject
      - status
      - updated
      - next
```

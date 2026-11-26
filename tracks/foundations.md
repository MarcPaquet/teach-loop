---
type: track
level: branch
---

# Foundations beneath my work

The gaps under what you already build or study: things you use but can't yet reason about from first principles.
**Starts empty.** The teacher adds a gap here when a lesson or probe exposes one. No deadline.

## Gaps found

*Found by the [[baseline]] probe, <YYYY-MM-DD>.*

- [ ] *A gap, in one line* → [[lesson-name]] (planned)

## Skills

Every skill this track needs, grouped by level. Set by the `tracks` property on each skill.

```base
filters:
  and:
    - file.inFolder("skills")
    - 'tracks.contains("foundations")'
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
    - 'tracks.contains("foundations")'
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

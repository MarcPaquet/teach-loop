# Learn: index

Start here. Notes live in `subjects/<subject>/`; practice sessions in `practice/`; explore trails in `explore/`;
tracks are goal pages that collect notes across subjects.

**Now:** *the track or lesson in progress.*

**Where I am:** [[baseline]], the probed map of your edges.

**What leads where:** [[skill-graph]], every skill and what it needs.

## In progress

```base
filters:
  and:
    - file.inFolder("subjects")
    - 'status == "in-progress"'
    - 'type != "playbook"'
views:
  - type: table
    name: In progress
    order:
      - file.name
      - next
      - updated
```

## Tracks

List tracks here, one line each, nested under the track they feed. Their order is the default for "what should I
learn next?" unless `LEARNER.md` sets a *Track order*.

- [[foundations]]: gaps found beneath current work
- [[example-track]]: a placeholder goal track (replace or delete)

## Subjects

One folder per subject under `subjects/`; list a subject here when its first note is created.

- *None yet.*

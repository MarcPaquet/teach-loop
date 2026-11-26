#!/usr/bin/env python3
"""Structure gate for the learning vault. Runs on what is staged, never the working tree.

Always checks the shape of skills/. Blocks structure changes unless the commit
message starts with "Structure:", which is used only after the learner approves the change.
"""
import re
import subprocess
import sys
from pathlib import PurePosixPath

MARKER = "Structure:"
KEYS = ["type", "domain", "level", "needs", "tracks", "lessons"]
LEVELS = {"unprobed", "none", "surface", "working", "solid"}
MAX_NEEDS = 3
PROCESS = (".claude/skills/", ".claude/agents/", ".githooks/", "CLAUDE.md", "LEARNER.md", "addons/", "skill-graph.md", "skill-lessons.base")
LESSON_WORK = ("subjects/", "practice/", "explore/")
NOTE_ROOTS_EXCLUDED = (".claude/", ".drills/")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def strip_comment(text):
    """Drop a trailing `# comment` (a # preceded by whitespace, outside quotes)."""
    quote = None
    for i, ch in enumerate(text):
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or text[i - 1].isspace()):
            return text[:i].rstrip()
    return text.strip()


LIST_KEYS = ("needs", "lessons", "tracks")


def clean(item):
    """One scalar or list item: no comment, no quotes, no [[ ]] (nor |alias or #heading inside)."""
    item = strip_comment(item).strip()
    if len(item) >= 2 and item[0] == item[-1] and item[0] in "\"'":
        item = item[1:-1].strip()
    if item.startswith("[[") and item.endswith("]]"):
        item = re.split(r"[|#]", item[2:-2], maxsplit=1)[0].strip()
    return item


def inline_list(text):
    """Items of `[a, "b", 'c']`, splitting on commas outside quotes."""
    items, current, quote = [], "", None
    for ch in text.strip()[1:-1]:
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch == ",":
            items.append(current)
            current = ""
            continue
        current += ch
    items.append(current)
    return [c for c in (clean(i) for i in items) if c]


def parse(text):
    """Frontmatter of a skill note, or None if there isn't any. Lists come back as lists of
    clean strings (inline or block), scalars as clean strings."""
    lines = text.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return None
    fields, key = {}, None
    for line in lines[1 : lines.index("---", 1)]:
        item = re.fullmatch(r"\s*- (.+)", line)
        if item and key and isinstance(fields[key], list):
            value = clean(item.group(1))
            if value:
                fields[key].append(value)
            continue
        pair = re.fullmatch(r"([a-z_]+):\s*(.*)", line)
        if not pair:
            return None
        key, value = pair.groups()
        value = strip_comment(value)
        if value == "":
            fields[key] = []
        elif value.startswith("[") and value.endswith("]") and not value.startswith("[["):
            fields[key] = inline_list(value)
        else:
            fields[key] = clean(value)
    for key in LIST_KEYS:  # a single value on a list key is a one-item list
        if isinstance(fields.get(key), str):
            fields[key] = [fields[key]] if fields[key] else []
    return fields


def skill_notes(paths, read):
    notes = {}
    for path in paths:
        p = PurePosixPath(path)
        if len(p.parts) == 3 and p.parts[0] == "skills" and p.suffix == ".md":
            notes[p.stem] = (p.parts[1], parse(read(path)))
    return notes


def shape_errors(notes, paths):
    errors = []
    md = [PurePosixPath(p) for p in paths if p.endswith(".md") and not p.startswith(NOTE_ROOTS_EXCLUDED)]
    seen = {}
    for p in md:
        seen.setdefault(p.stem.lower(), []).append(str(p))
    errors += [f"same filename: {', '.join(v)}" for v in seen.values() if len(v) > 1]
    subjects = {p.stem for p in md if p.parts[0] == "subjects"}
    tracks = {p.stem for p in md if p.parts[0] == "tracks"}
    graph = {}
    for name, (folder, fields) in notes.items():
        if fields is None:
            errors.append(f"{name}: no readable frontmatter")
            continue
        if list(fields) != KEYS:
            errors.append(f"{name}: properties must be {', '.join(KEYS)}")
            continue
        if fields["type"] != "skill":
            errors.append(f"{name}: type must be skill")
        if fields["domain"] != folder:
            errors.append(f"{name}: domain must match its folder ({folder})")
        if fields["level"] not in LEVELS:
            errors.append(f"{name}: unknown level {fields['level']}")
        needs = fields["needs"]
        graph[name] = needs
        if len(needs) > MAX_NEEDS:
            errors.append(f"{name}: more than {MAX_NEEDS} needs")
        errors += [f"{name}: needs unknown skill {n}" for n in needs if n not in notes]
        errors += [f"{name}: unknown lesson {l}" for l in fields["lessons"] if l not in subjects]
        on = fields["tracks"]
        if not on:
            errors.append(f"{name}: needs at least one track")
        errors += [f"{name}: unknown track {t}" for t in on if t not in tracks]
    state = {}

    def visit(name, path):
        if state.get(name) == 2 or name not in graph:
            return
        if state.get(name) == 1:
            errors.append("cycle: " + " -> ".join(path + [name]))
            return
        state[name] = 1
        for need in graph[name]:
            visit(need, path + [name])
        state[name] = 2

    for name in graph:
        visit(name, [])
    return errors


def main():
    message = open(sys.argv[1], encoding="utf-8").read()
    approved = message.lstrip().startswith(MARKER)
    staged = git("ls-files").splitlines()
    changed = [p for p in git("diff", "--cached", "--name-only").splitlines() if PurePosixPath(p).name != ".gitkeep"]
    new = skill_notes(staged, lambda p: git("show", f":{p}"))
    old = skill_notes(git("ls-tree", "-r", "--name-only", "HEAD").splitlines(), lambda p: git("show", f"HEAD:{p}"))

    errors = shape_errors(new, staged)
    structure = [f"process file changed: {p}" for p in changed if p.startswith(PROCESS)]
    structure += [f"skill added: {n}" for n in new.keys() - old.keys()]
    structure += [f"skill removed: {n}" for n in old.keys() - new.keys()]
    level_moved = False
    for name in new.keys() & old.keys():
        (folder_new, a), (folder_old, b) = new[name], old[name]
        if folder_new != folder_old:
            structure.append(f"skill moved: {name}")
        if a and b:
            if sorted(a.get("needs", [])) != sorted(b.get("needs", [])):
                structure.append(f"needs changed: {name}")
            level_moved = level_moved or a.get("level") != b.get("level")

    if level_moved and "baseline.md" not in changed:
        errors.append("a skill's level changed without baseline.md, its source of truth, in the same commit")
    if any(p.startswith(PROCESS) for p in changed) and any(p.startswith(LESSON_WORK) for p in changed):
        errors.append("process changes get their own commit, without lesson or practice notes")
    if structure and not approved:
        errors += structure
        errors.append(f'structure changes need the learner\'s approval, then a message starting with "{MARKER}"')

    if errors:
        print("Structure gate blocked this commit:", file=sys.stderr)
        print("\n".join(f"  - {e}" for e in errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

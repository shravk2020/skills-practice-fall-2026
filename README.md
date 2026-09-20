# Python / FastAPI / ML Lab

A guided, 8-week, day-by-day practice lab: Python fundamentals → FastAPI & httpx →
ML techniques → databases → DevOps → full-stack integration → a capstone project.
Built after an App Dev Club technical interview (FastAPI + pytest + httpx, clone-a-repo-
and-pass-the-tests format) went rough, to build real fluency instead of memorized syntax.

## How this works

Each day is its own folder: `dayNN-topic-name/`. Every folder has:
- **README.md** — the lesson: why it matters, where it shows up in real jobs, the
  syntax and concepts you need with links to the official docs, the task itself,
  common pitfalls, and a stretch goal.
- **starter.py** (or **main.py** for FastAPI days) — a stub with `TODO`s. This is
  the only file you edit.
- **test_starter.py** (or **test_main.py**) — a pre-written test suite. Don't edit
  this. Run `pytest`, watch it fail, make it pass. This mirrors the ADC interview
  format on purpose.
- **solution.py** — a reference implementation. Don't open it until you're done or
  genuinely stuck — the point is building the muscle, not copying it.

### One-time setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Each day
```bash
cd dayNN-topic-name
pytest -v          # see it fail
# ...edit starter.py...
pytest -v          # get it green
```

## Progress

### Foundations — do these before Day 1
Week 1 jumps straight to comprehensions, decorators, and dunder methods on
the assumption you're already fluent in the base mechanics. These four days
cover that base layer properly: every list/dict/set/string method, and real
class construction (instance vs. class attributes, `@classmethod`,
`@staticmethod`, inheritance).
- [ ] [Day 0a — Lists, deep dive](day00a-lists-deep-dive/)
- [ ] [Day 0b — Dictionaries, deep dive](day00b-dicts-deep-dive/)
- [ ] [Day 0c — Tuples, sets & strings](day00c-tuples-sets-strings/)
- [ ] [Day 0d — Classes & method construction](day00d-classes-and-methods/)

### Week 1 — Python Fundamentals & Idioms
- [ ] [Day 1 — Pythonic data structures](day01-pythonic-data-structures/)
- [ ] [Day 2 — Functions, closures, decorators](day02-decorators/)
- [ ] [Day 3 — OOP done right](day03-oop-dataclasses-dunders/)
- [ ] [Day 4 — Type hints & static analysis](day04-type-hints-mypy/)
- [ ] [Day 5 — Errors & context managers](day05-errors-context-managers/)

### Week 2 — Stdlib, Async, Testing
- [ ] [Day 6 — Iterators & generators](day06-iterators-generators/)
- [ ] [Day 7 — Files & CLI tools](day07-files-cli-tools/)
- [ ] [Day 8 — Async fundamentals](day08-async-fundamentals/)
- [ ] [Day 9 — Packaging & environments](day09-packaging-environments/)
- [ ] [Day 10 — Testing with pytest](day10-testing-with-pytest/)

### Week 3 — FastAPI & httpx
- [ ] [Day 11 — FastAPI CRUD basics](day11-fastapi-crud-basics/)
- [ ] Day 12 — Pydantic deep dive *(coming soon)*
- [ ] Day 13 — Routers, dependencies, middleware *(coming soon)*
- [ ] Day 14 — httpx as a client *(coming soon)*
- [ ] Day 15 — Testing FastAPI properly *(coming soon)*

### Week 4 — ML Techniques
- [ ] Day 16 — Algorithms from scratch *(coming soon)*
- [ ] Day 17 — Proper evaluation *(coming soon)*
- [ ] Day 18 — Feature engineering pipelines *(coming soon)*
- [ ] Day 19 — Intro to PyTorch *(coming soon)*
- [ ] Day 20 — Serving a model cleanly *(coming soon)*

### Week 5 — Databases
- [ ] Day 21 — SQL fundamentals *(coming soon)*
- [ ] Day 22 — sqlite3 from Python, safely *(coming soon)*
- [ ] Day 23 — MongoDB basics *(coming soon)*
- [ ] Day 24 — ORMs *(coming soon)*
- [ ] Day 25 — Migrations & schema evolution *(coming soon)*

### Week 6 — DevOps
- [ ] Day 26 — Git workflows *(coming soon)*
- [ ] Day 27 — Docker basics *(coming soon)*
- [ ] Day 28 — Config & secrets *(coming soon)*
- [ ] Day 29 — CI with GitHub Actions *(coming soon)*
- [ ] Day 30 — Cloud deployment *(coming soon)*

### Week 7 — Full-Stack Integration
- [ ] Day 31 — React/Vite refresher *(coming soon)*
- [ ] Day 32 — Forms & mutations *(coming soon)*
- [ ] Day 33 — Auth basics *(coming soon)*
- [ ] Day 34 — Deploying the frontend *(coming soon)*
- [ ] Day 35 — Polish pass *(coming soon)*

### Week 8 — Capstone + Interview Practice
- [ ] Days 36-39 — Capstone build *(its own repo once started, see root plan)*
- [ ] Day 40 — Timed interview drill + retro *(coming soon)*

Full day-by-day plan and rationale also tracked in `shravani-os` (private repo):
`knowledge/skills/python-fastapi-ml-mastery-plan.md`.

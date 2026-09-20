# Day 9 — Packaging & Environments

## Why this matters
Every script you've written so far only runs as `python3 starter.py`. Real
tools get installed and run as a plain command (`pytest`, `black`, `uvicorn`
all work this way). Today's task is different from the others: the *code* is
already written and correct — your job is entirely the packaging
configuration, because that's the actual skill this day is teaching.

## Where you'll actually use this
- **Any Python project with more than one file** needs a real package
  structure, not a folder of loose scripts — this is table stakes for
  anything you'd put on a resume or deploy.
- **Internal company tools**: a lot of real engineering work is "make this
  script into a command my team can `pip install` and run," not just writing
  the logic once.
- **Understanding what pip actually does**: after today, `pip install -e .`
  stops being a magic incantation you copy from Stack Overflow.

## Concepts & syntax

### `pyproject.toml`
The modern, standard way to describe a Python package: its name, version,
dependencies, and — relevant today — what commands it should install.
Docs: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

### `[project.scripts]` — console entry points
```toml
[project.scripts]
notes = "notes_cli:main"
```
This line is what turns `python3 notes_cli.py somefile.txt` into just
`notes somefile.txt` as a real installed command. The format is
`command-name = "module_name:function_name"` — pip generates a tiny
executable that imports that module and calls that function.
Docs: https://packaging.python.org/en/latest/specifications/entry-points/

### Editable installs
```bash
pip install -e .
```
Installs your package "in place" — pip doesn't copy your files anywhere,
it just makes `notes_cli` importable and creates the `notes` command,
pointing both at your actual source folder. Edit the source, rerun
immediately, no reinstall needed. This is what you use during development;
a normal (non-editable) `pip install .` is what you'd do to actually ship it.
Docs: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs

## The task
1. Read `notes_cli.py` — it's already fully implemented, nothing to fix there.
2. Open `pyproject.toml` — it has two `TODO`s: the `[project] name` field
   (pick anything, e.g. `"notes-cli-lab"`) and the `[project.scripts]` entry
   point (needs to point `notes` at the `main` function inside `notes_cli`).
3. From inside this folder, with your lab's venv active, run:
   ```bash
   pip install -e .
   ```
4. Confirm the installed command works from anywhere (not just
   `python3 notes_cli.py`):
   ```bash
   echo -e "buy milk\nwalk dog\n" > /tmp/notes.txt
   notes /tmp/notes.txt
   # should print: 2 notes found in /tmp/notes.txt
   ```
5. Run `pytest` — this tests the underlying logic directly (it doesn't
   depend on step 3), so it should already pass even before you touch
   `pyproject.toml`. The manual steps above are the actual exercise.

## Run it
```bash
cd day09-packaging-environments
pytest -v                 # tests the logic directly, should already pass
pip install -e .          # after filling in the TODOs in pyproject.toml
notes /tmp/notes.txt      # confirm the installed command works
```

## Common pitfalls
- If `pip install -e .` fails with something about `setuptools` not finding
  your module, double check `[tool.setuptools] py-modules = ["notes_cli"]` —
  for a single-file package like this one (no `src/` folder), setuptools
  needs to be told explicitly which top-level module to include.
- If the `notes` command isn't found after installing, make sure you're still
  in the same virtual environment you installed it into — entry-point
  scripts get installed into that venv's `bin/` folder specifically.
- A typo in the entry point string (e.g. `"notes_cli.main"` with a dot
  instead of a colon) is the most common mistake — it's always
  `module:function`, colon not dot.

## Verify it worked
Check off each of these for yourself (no automated test covers steps 3-4):
- [ ] `pyproject.toml` TODOs filled in
- [ ] `pip install -e .` completes with no errors
- [ ] `notes /tmp/notes.txt` runs as a bare command and prints the right count
- [ ] `pytest` passes

If you get stuck, `solution/pyproject.toml` has the filled-in reference.

## Stretch goal (optional)
Add a `[project.optional-dependencies]` section with a `dev` extra that
includes `pytest` and `mypy`, so a future user could run
`pip install -e ".[dev]"` to get both your tool and its dev tooling in one
command. This is the real-world pattern for separating "what the tool needs
to run" from "what you need to develop it."

## Further reading
- Python Packaging Authority's full tutorial (the authoritative source):
  https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Day 11 — FastAPI CRUD Basics

## Why this matters
This is the exact shape of your ADC interview: a FastAPI app with routes you
implement, checked against a pre-written test suite. Today builds a full
CRUD (Create, Read, Update, Delete) API for a simple "notes" resource — the
single most common shape of a backend API, and the foundation the rest of
this week builds on directly (Day 12 adds richer validation to these same
notes, Day 13 restructures this same app into modules).

## Where you'll actually use this
- **This is what a backend internship actually is**, day to day: define a
  resource, expose CRUD endpoints for it, validate input, return the right
  status codes.
- **Every framework has this pattern** (Django REST Framework, Express,
  Rails) — FastAPI's version is unusually explicit about types and
  validation, which is exactly why it's a good one to learn this on.

## Concepts & syntax

### Defining the app and routes
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    ...
```
`item_id: int` in both the path (`{item_id}`) and the function signature
means FastAPI automatically converts the URL segment to an `int` and returns
a `422` automatically if someone passes something that isn't one — you get
that validation for free just by adding the type hint.
Docs: https://fastapi.tiangolo.com/tutorial/path-params/

### Query parameters
```python
@app.get("/items")
def list_items(limit: int = 10, offset: int = 0):
    ...
```
Any function parameter that *isn't* part of the path automatically becomes a
query parameter (`/items?limit=5&offset=10`), with the default value making
it optional. **When to use this:** pagination, filtering, sorting — anything
that shapes *which* results come back, not *which resource* you mean (that's
what the path is for).
Docs: https://fastapi.tiangolo.com/tutorial/query-params/

### Request bodies with Pydantic
```python
from pydantic import BaseModel

class NoteIn(BaseModel):
    title: str

@app.post("/notes")
def create_note(note: NoteIn):
    ...
```
A `BaseModel` parameter (not in the path or given a default) is read from
the JSON request body and validated automatically — send `{"title": 123}`
and FastAPI rejects it with a `422` before your function even runs, no
manual `if` checks needed.
Docs: https://fastapi.tiangolo.com/tutorial/body/

### Status codes and errors
```python
from fastapi import HTTPException

@app.post("/notes", status_code=201)
def create_note(note: NoteIn):
    ...

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in store:
        raise HTTPException(status_code=404, detail="note not found")
    ...
```
`status_code=201` on the decorator sets the *success* status code (`201
Created` is the correct code for a POST that creates something — `200` is
technically wrong there, even though it "works"). `HTTPException` is how you
return an *error* status code from inside the function body.
Docs: https://fastapi.tiangolo.com/tutorial/handling-errors/

## The task
Open `main.py`. There's an in-memory `NoteStore` already provided (don't
change it) and two Pydantic models (`NoteIn`, `Note`). Implement:
- `GET /notes` — return notes, respecting `limit`/`offset` query params, in
  insertion order.
- `GET /notes/{note_id}` — return one note, or `404` if it doesn't exist.
- `POST /notes` (status 201) — create a note with an auto-incrementing id.
- `PUT /notes/{note_id}` — update a note's title, or `404` if it doesn't exist.
- `DELETE /notes/{note_id}` (status 204) — delete a note, or `404` if it
  doesn't exist.

## Run it
```bash
cd day11-fastapi-crud-basics
pytest -v
```
Notice `test_main.py` has an `autouse=True` fixture that resets `store`
before every test — without it, notes created in one test would leak into
the next, since `store` is a single shared object for the whole app's
lifetime. This is a real pattern you'll use constantly once you add a real
database in Week 5.

You can also run the server for real and poke at it in the browser:
```bash
uvicorn main:app --reload
# then open http://127.0.0.1:8000/docs
```
FastAPI auto-generates that `/docs` page (Swagger UI) from your type hints
and models — it's a free interactive API tester, worth keeping open while
you build.

## Common pitfalls
- Forgetting `status_code=201`/`204` on the decorator — the tests check for
  the *correct* REST status code, not just "some success code."
- `DELETE` with `status_code=204` means your function should return `None` —
  FastAPI won't include a body for a 204 response even if you try to return
  one.
- Route order matters when paths could overlap (not an issue with today's
  routes, but worth knowing): FastAPI matches routes top-to-bottom, so a more
  specific path needs to be declared before a more general one that could
  also match it.

## Stretch goal (optional)
Add a `GET /notes/count` endpoint that returns `{"count": <total notes>}`.
Then notice the trap: if you declare it *after* `GET /notes/{note_id}`,
requests to `/notes/count` get swallowed by the `{note_id}` route instead
(FastAPI tries to convert `"count"` to an `int` and fails with a confusing
422). Move the declaration above `/notes/{note_id}` to fix it — this is the
route-ordering issue mentioned above, now made concrete.

## Further reading
- FastAPI's own tutorial (excellent, worth reading in full over time):
  https://fastapi.tiangolo.com/tutorial/
- HTTP status code reference (know at least the common ones by heart):
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

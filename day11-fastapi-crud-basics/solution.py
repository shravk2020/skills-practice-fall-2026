from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class NoteIn(BaseModel):
    title: str


class Note(NoteIn):
    id: int


class NoteStore:
    def __init__(self):
        self.notes: dict[int, dict] = {}
        self.next_id = 1

    def reset(self):
        self.notes = {}
        self.next_id = 1


store = NoteStore()


@app.get("/notes")
def list_notes(limit: int = 10, offset: int = 0):
    items = list(store.notes.values())
    return items[offset: offset + limit]


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    note = store.notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@app.post("/notes", status_code=201)
def create_note(note: NoteIn):
    note_id = store.next_id
    store.next_id += 1
    created = {"id": note_id, "title": note.title}
    store.notes[note_id] = created
    return created


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn):
    existing = store.notes.get(note_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="note not found")
    existing["title"] = note.title
    return existing


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in store.notes:
        raise HTTPException(status_code=404, detail="note not found")
    del store.notes[note_id]

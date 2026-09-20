from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class NoteIn(BaseModel):
    title: str


class Note(NoteIn):
    id: int


class NoteStore:
    """Given -- don't modify. A simple in-memory store standing in for a
    real database until Week 5."""

    def __init__(self):
        self.notes: dict[int, dict] = {}
        self.next_id = 1

    def reset(self):
        self.notes = {}
        self.next_id = 1


store = NoteStore()


@app.get("/notes")
def list_notes(limit: int = 10, offset: int = 0):
    """Return notes in insertion order, respecting limit/offset.

    TODO: implement.
    """
    pass


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Return the note with this id, or raise HTTPException(404) if it
    doesn't exist.

    TODO: implement.
    """
    pass


@app.post("/notes", status_code=201)
def create_note(note: NoteIn):
    """Create a new note with an auto-incrementing id, store it, return it.

    TODO: implement.
    """
    pass


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn):
    """Update the existing note's title. Raise HTTPException(404) if it
    doesn't exist. Return the updated note.

    TODO: implement.
    """
    pass


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    """Delete the note. Raise HTTPException(404) if it doesn't exist.
    Return nothing (204 No Content).

    TODO: implement.
    """
    pass

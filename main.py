from fastapi import FastAPI, HTTPException
from bson import ObjectId
from database import collection, format_data, Notes

app = FastAPI()

@app.get("/")
async def get_notes():
    notes = []
    for note in collection.find():
        notes.append(format_data(note))
    return notes

@app.get("/{note_id}")
async def get_note_by_id(note_id: str):
    note = collection.find_one({"_id": ObjectId(note_id)})
    if note:
        return format_data(note)
    raise HTTPException(status_code=404, detail="Note not found")

@app.post("/")
async def create_note(note: Notes):
    new_note = {
        "note": note.note
    }
    result = collection.insert_one(new_note)
    created_note = collection.find_one({"_id": result.inserted_id})
    return format_data(created_note)

@app.delete("/{note_id}")
async def delete_note_by_id(note_id: str):
    result = collection.delete_one({"_id": ObjectId(note_id)})
    if result.deleted_count == 1:
        return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")

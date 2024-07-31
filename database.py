import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
password = os.getenv("PASSWORD")
id = f"mongodb+srv://Mycin:{password}@cluster0.yzel00n.mongodb.net"
conn = MongoClient(id)

collection = conn.notes.notes

class Notes(BaseModel):
    id: str
    note: str

def formatData(note) -> dict:
    return {
        "id": str(note["_id"]),
        "note": note["note"]
    }

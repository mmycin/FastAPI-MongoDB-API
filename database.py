import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
password = os.getenv("PASSWORD")
user = os.getenv("USER")
id = f"mongodb+srv://{user}:{password}@cluster0.yzel00n.mongodb.net"
conn = MongoClient(id)

collection = conn.notes.notes

class Notes(BaseModel):
    id: str
    note: str

def format_data(note) -> dict:
    return {
        "id": str(note["_id"]),
        "note": note["note"]
    }

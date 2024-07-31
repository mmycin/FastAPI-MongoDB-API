from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Notes, collection, formatData

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=list[Notes])
async def home():
    doc_list: list = []
    for doc in collection.find({}):
        doc_list.append(formatData(doc))
    return doc_list

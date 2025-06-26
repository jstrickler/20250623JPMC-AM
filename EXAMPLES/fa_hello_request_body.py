from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect("wombats.db")
cursort = conn.cursor()

INSERT = "insert into wombats (name, age) values (?, ?)"

all_wombats = {}

class Wombat(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/wombats", status_code=201)
async def add_wombat(wombat: Wombat):
    if wombat.name in all_wombats:  # query DB for dupes
        raise HTTPException(status_code=400, detail="Duplicate wombat name")
    all_wombats[wombat.name] = wombat  # insert new record
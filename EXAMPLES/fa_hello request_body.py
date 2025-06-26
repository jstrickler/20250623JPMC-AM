from fastapi import FastAPI
from pydantic import BaseModel

class Wombat(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/wombats")
async def add_wombat(wombat: Wombat):
    return wombat
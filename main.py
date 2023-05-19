from typing import Optional, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uuid

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class Articolo(BaseModel):
    id: Optional[str]
    model: str
    description: str | None = None

articoli = [
    Articolo(id = str(uuid.uuid4()), model = 'Scarpa invernale'),
    Articolo(id = str(uuid.uuid4()), model = 'Scarpa invernale')
]

@app.get("/articoli")
def get_articoli():
    return articoli

@app.get("/articoli/{id}")
def get_articoli_by_id(id: str):
    for articolo in articoli:
        if articolo.id == id:
            return articolo
    return None

@app.post("/articoli")
def post_articoli(articolo: Articolo):
    articolo.id = str(uuid.uuid4())
    articoli.append(articolo)
    return articolo

@app.put("/articoli/{id}")
def put_articoli(id:str, art: Articolo):
    for articolo in articoli:
        if articolo.id == id:
            articolo.model = art.model
            return articolo
    return None

@app.delete("/articoli/{id}")
def delete_articoli_by_id(id: str):
    for articolo in articoli:
        if articolo.id == id:
            articoli.remove(articolo)
    return None
# FILE: server.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MahasiswaItem(BaseModel):
    nama: str
    nim: str
    jurusan: str

database = []

@app.get("/mahasiswa")
def ambil_data():
    return database

@app.post("/mahasiswa")
def kirim_data(item: MahasiswaItem):
    database.append(item)
    return {"pesan": "Data masuk"}
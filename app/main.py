from fastapi import FastAPI
from app.engine.body import analisar_jogo

app = FastAPI(title="Intensímetro API")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/scan/match")
def scan_match(match_id: int):
    return analisar_jogo(match_id)

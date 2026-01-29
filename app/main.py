from fastapi import FastAPI
from app.engine.body import analisar_jogo

app = FastAPI(title="Intensimetro API")

@app.get("/")
def health():
    return {"status": "ok"}

# 🔥 ROTA FÁCIL PRA TESTE (GET)
@app.get("/scan")
def scan(match_id: int):
    return analisar_jogo(match_id)

from app.engine.heart import calcular_medias
from app.engine.mind import avaliar_contexto

def analisar_jogo(match_id: int):
    dados = {
        "media_gols": 2.8,
        "media_gols_1t": 1.1,
        "media_esc": 9,
        "media_esc_1t": 4,
        "media_cartoes": 3.4,
        "decisivo": True,
        "forma_instavel": True,
        "variancia_alta": True
    }

    medias = calcular_medias(dados)
    mente = avaliar_contexto(dados)

    return {
        "match_id": match_id,
        "medias": medias,
        **mente
    }

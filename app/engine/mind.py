def avaliar_contexto(dados):
    risco = "baixo"

    if dados["decisivo"] or dados["variancia_alta"]:
        risco = "alto"
    elif dados["forma_instavel"]:
        risco = "medio"

    return {
        "decisivo": dados["decisivo"],
        "forma_instavel": dados["forma_instavel"],
        "variancia_alta": dados["variancia_alta"],
        "risco_aposta": risco
    }

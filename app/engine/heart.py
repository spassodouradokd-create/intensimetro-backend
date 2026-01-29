def calcular_medias(dados):
    return {
        "gols": dados["media_gols"],
        "gols_1t": dados["media_gols_1t"],
        "escanteios": dados["media_esc"],
        "escanteios_1t": dados["media_esc_1t"],
        "cartoes": dados["media_cartoes"]
    }

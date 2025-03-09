estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}
estacoes["conjunto1"] = set(["id", "nv", "ut"])
estacoes["conjunto2"] = set(["wa", "id", "mt"])
estacoes["conjunto3"] = set(["or", "nv", "ca"])
estacoes["conjunto4"] = set(["nv", "ut"])
estacoes["conjunto5"] = set(["ca", "az"])

def coberturaEstacoes(estados_abranger, estacoes):
    estacoes_final = set()
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados_por_estacao in estacoes.items():
            cobertos = estados_abranger & estados_por_estacao
            if len(cobertos) > len(estados_cobertos) and estacao not in estacoes_final:
                melhor_estacao = estacao
                estados_cobertos = cobertos
        if melhor_estacao is not None:
            estados_abranger -= estados_cobertos
            estacoes_final.add(melhor_estacao)
            estacoes.pop(melhor_estacao)
        else:
            return None
    return estacoes_final

print(coberturaEstacoes(estados_abranger, estacoes))

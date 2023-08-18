def encontrarVencedores(votos_candidato1, votos_candidato2, votos_candidato3):
    if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
        return ["Candidato 1"]
    elif votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3:
        return ["Candidato 2"]
    elif votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2:
        return ["Candidato 3"]
    elif votos_candidato1 == votos_candidato2 and votos_candidato1 > votos_candidato3:
        return ["Candidato 1", "Candidato 2"]
    elif votos_candidato1 == votos_candidato3 and votos_candidato1 > votos_candidato2:
        return ["Candidato 1", "Candidato 3"]
    elif votos_candidato2 == votos_candidato3 and votos_candidato2 > votos_candidato1:
        return ["Candidato 2", "Candidato 3"]
    else:
        return ["Candidato 1", "Candidato 2", "Candidato 3"]

votos_candidato1 = 150
votos_candidato2 = 120
votos_candidato3 = 150

vencedores = encontrarVencedores(votos_candidato1, votos_candidato2, votos_candidato3)

if len(vencedores) == 1:
    print("O vencedor é:", vencedores[0])
else:
    print("Empate entre os candidatos:", ", ".join(vencedores))

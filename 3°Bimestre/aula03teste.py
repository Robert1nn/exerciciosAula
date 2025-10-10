def participantes(numParticipantes):
    if numParticipantes < 0:
        return "Número de participantes inválido."
    elif numParticipantes <= 5:
        return "Sala Pequena (até 5 pessoas)."
    elif numParticipantes <= 15:
        return "Sala Média (de 6 a 15 pessoas)."
    else:
        return "Sala Grande (mais de 15 pessoas)."
def recomendar_sala(salas):
    if salas.lower() == "executiva":
        return "Sala Grande (reuniões executivas precisam de mais espaço)."
    elif salas.lower() == "normal":
        return "Sala Pequena (reuiniões normais podem ser em salas pequenas ou medias)."
    else:
        return "Erro, não existe essa opção"

num = int(input("Digite o número de participantes: "))
recomendacaoParticipantes = participantes(num)

tipo = input("Digite o tipo de reunião (normal/executiva): ")
recomendacaoTipo = recomendar_sala(ti0po) 
print(f"Quantidades dos participantes: {recomendacaoParticipantes} A recomendação da salas são: {recomendacaoTipo}")
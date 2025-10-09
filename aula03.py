def recomendar_sala(numParticipantes, reuniao):
    if numParticipantes < 0:
        return "Número de participantes inválido."
    elif reuniao == "executiva":
        return "Sala Grande (reuniões executivas precisam de mais espaço)."
    elif reuniao == "normal":
        return "Sala Pequena (reuiniões normais podem ser em salas pequenas ou medias)"
    elif numParticipantes <= 5:
        return "Sala Pequena (até 5 pessoas)."
    elif numParticipantes <= 15:
        return "Sala Média (de 6 a 15 pessoas)."
    else:
        return "Sala Grande (mais de 15 pessoas)."

# Programa principal   
print("====== Sistemas de recomendação ==========")
numero = int(input("Digite o número de participantes: "))
tipo = input("Digite o tipo de reunião (normal/executiva): ")

recomendacao = recomendar_sala(numero, tipo)
print(f"A recomendação eh: {recomendacao}")
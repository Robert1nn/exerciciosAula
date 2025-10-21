#Criar um vetor (lista) com tamanho fixo
notas = [0, 0, 0, 0, 0]  

#ler 5 notas e guardar nas posições certas
for i in range(6):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas[i] = nota  # insere manualmente na posição

soma = 0
for i in range(6):
    soma = soma + notas[i]

#Sabemos que são 5 notas, então dividimos por 5
media = soma / 5

#mostrar resultados
print(f"\nA média das notas é: {media:.2f}")

print("\nNotas acima da média:")
for i in range(5):
    if notas[i] > media:
        print(notas[i])

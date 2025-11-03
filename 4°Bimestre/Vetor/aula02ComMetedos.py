# Começamos com uma lista vazia
notas = []

# Loop para ler 5 notas
for i in range(10):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota) # Adiciona a nota ao final da lista

# A função sum() é a forma mais fácil de somar os itens de uma lista
soma = sum(notas)

# Calcula a média
media = soma / len(notas)

print(f"\nA média das notas é: {media:.2f}")

print("\nNotas acima da média:")
for nota in notas:
    if nota > media:
        print(f"{nota:.1f}")
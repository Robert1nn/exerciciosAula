numeros = [0, 0, 0, 0, 0]

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros[i] = numero

print("\nOs números digitados foram:")
for i in range(5):
    print(numeros[i])

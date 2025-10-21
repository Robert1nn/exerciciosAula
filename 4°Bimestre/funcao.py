# Cria uma matriz 3x4 de assentos livres (0)
sala = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Mostra o mapa atual
print("Mapa inicial:")
for linha in sala:
    print(linha)

# Recebe a posição para reserva
fileira = int(input("Digite a fileira (0-2): "))
assento = int(input("Digite o assento (0-3): "))

# Atualiza o assento
sala[fileira][assento] = 1

# Mostra o mapa atualizado
print("\nMapa atualizado:")
for linha in sala:
    print(linha)

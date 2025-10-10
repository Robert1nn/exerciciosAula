# Vetor inicial de estoque
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender(produto, quantidade):
    estoque[produto - 1] = estoque[produto - 1] - quantidade

# Função para adicionar produtos
def adicionar(produto, quantidade):
    estoque[produto - 1] = estoque[produto - 1] + quantidade

# Função para exibir o estoque
def exibir():
    print("\nEstoque atual:")
    for i in range(5):  # 5 produtos
        print("Produto", i + 1, "→", estoque[i], "unidades")

# --- Operações solicitadas ---
vender(1, 3)   # vendeu 3 do produto 1
vender(4, 2)   # vendeu 2 do produto 4
adicionar(5, 10)  # adicionou 10 ao produto 5

# --- Mostrar o resultado ---
exibir()

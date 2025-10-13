#VETOR INICIAL
estoque = [20, 15, 10, 30, 5]  

def vender(produto, quantidade):
    estoque[produto] = estoque[produto] - quantidade

def adicionar(produto, quantidade):
    estoque[produto] = estoque[produto] + quantidade

def mostrar_estoque():
    print("\n:")
    print("Produto 1:", estoque[0], "unidades")
    print("Produto 2:", estoque[1], "unidades")
    print("Produto 3:", estoque[2], "unidades")
    print("Produto 4:", estoque[3], "unidades")
    print("Produto 5:", estoque[4], "unidades")

# Vende 3 unidades do produto 1
vender(0, 3)

# Vende 2 unidades do produto 4
vender(3, 2)

# Adiciona 10 unidades ao produto 5
adicionar(4, 10)

mostrar_estoque()

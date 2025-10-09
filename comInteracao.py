class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_cor(self):
        return self.__cor

    def get_preco(self):
        return self.__preco

    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def set_preco(self, novo_preco):
        self.__preco = novo_preco


# Pedindo dados ao usuário
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano do carro: "))
cor = input("Digite a cor do carro: ")
preco = float(input("Digite o preço do carro: "))

# Criando objeto com os dados informados
carro1 = Carro(marca, modelo, ano, cor, preco)

# Mostrando informações
print("\n--- Informações do carro ---")
print("Marca:", carro1.get_marca())
print("Modelo:", carro1.get_modelo())
print("Ano:", carro1.get_ano())
print("Cor:", carro1.get_cor())
print("Preço:", carro1.get_preco())

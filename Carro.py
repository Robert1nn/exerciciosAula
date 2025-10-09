class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco

    # Getter e Setter - marca
    def get_marca(self):
        return self.__marca
    def set_marca(self, nova_marca):
        self.__marca = nova_marca
    
    # Getter e Setter - modelo
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    # Getter e Setter - ano
    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        if novo_ano > 1885:  # primeiro carro inventado em 1886
            self.__ano = novo_ano
        else:
            print("Ano inválido para um carro!")

    # Getter e Setter - cor
    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    # Getter e Setter - preço
    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço não pode ser negativo!")

# Criando um carro
carro1 = Carro("Toyota", "Corolla", 2020, "Prata", 95000)

# Testando getters
print("Marca:", carro1.get_marca())
print("Modelo:", carro1.get_modelo())
print("Ano:", carro1.get_ano())
print("Cor:", carro1.get_cor())
print("Preço:", carro1.get_preco())

# Alterando valores com setters
carro1.set_marca("Honda")
carro1.set_modelo("Civic")
carro1.set_ano(2023)
carro1.set_cor("Preto")
carro1.set_preco(120000)

print("\nApós alterações:")
print("Marca:", carro1.get_marca())
print("Modelo:", carro1.get_modelo())
print("Ano:", carro1.get_ano())
print("Cor:", carro1.get_cor())
print("Preço:", carro1.get_preco())

# Testando validações
print("\nTestando valores inválidos:")
carro1.set_ano(2000)   # inválido
carro1.set_preco(1000) # inválido


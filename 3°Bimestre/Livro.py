class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__preco = preco

    # Getter para titulo
    def get_titulo(self):
        return self.__titulo
    # Setter para titulo
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    # Getter para autor
    def get_autor(self):
        return self.__autor
    # Setter para autor
    def set_autor(self, novo_autor):
        self.__autor = novo_autor
    # Getter para autor
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    # Setter para autor
    def set_ano_publicacao(self, nova_publicacao):
        self.__ano_publicacao = nova_publicacao
     # Getter para autor
    def get_preco(self):
        return self.__preco
    # Setter para autor
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    # Criando um carro
livro1 = Livro("Jogo vorazes", "Suzanne Collins", 14.2008, 18.44)

# Testando getters
print("Titulo: ", livro1.get_titulo())
print("Autor: ", livro1.get_autor())
print("Ano da publicação do livro: ", livro1.get_ano_publicacao())
print("Preço: ", livro1.get_preco())

# Alterando valores com setters
livro1.set_titulo("O Seminarista")
livro1.set_autor("Bernardo Guimarães")
livro1.set_ano_publicacao(1872)
livro1.set_preco(10.04)

print("\nApós alterações:")
print("Marca:", livro1.get_titulo())
print("Autor:", livro1.get_autor())
print("Ano:", livro1.get_ano_publicacao())
print("Preço:", livro1.get_preco())

# Testando validações
# print("\nTestando valores inválidos:")
# livro1.set_ano(2000)   # inválido
# carro1.set_preco(1000) # inválido

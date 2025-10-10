def estoque(self, produto, quantidade):
    if produto in self.estoque:
        self.estoque[produto] += quantidade
    else:
        self.estoque[produto] = quantidade
    print(f"Estoque atualizado: {produto} - {self.estoque[produto]} unidades")
def vender(self, produto, quantidade):
    if produto in self.estoque and self.estoque[produto] >= quantidade:
        self.estoque[produto] -= quantidade
        print(f"Venda realizada: {produto} - {quantidade} unidades")
    else:
        print(f"Venda não realizada: estoque insuficiente para {produto}")# Classe para gerenciar o estoque de uma loja
def exibirQuantidade(self, produto):
    if produto in self.estoque:
        print(f"Quantidade em estoque de {produto}: {self.estoque[produto]} unidades")
    else:
        print(f"{produto} não está no estoque")
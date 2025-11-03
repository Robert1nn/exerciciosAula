# Vetor com as vendas mensais (12 meses)
vendas = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

# 1. Calcular o total anual de vendas
total = 0
for n in vendas:
    total += n

# 2. Calcular a média mensal de vendas
quantidade_meses = len(vendas)
media = total / quantidade_meses

# 3. Determinar o mês com a maior venda
maior_venda = vendas[0]
mes_maior = 0

for i in range(1, quantidade_meses):
    if vendas[i] > maior_venda:
        maior_venda = vendas[i]
        mes_maior = i

# Exibir os resultados
print("Total anual de vendas:", total)
print("Média mensal de vendas:", media)
print("Mês com a maior venda:", mes_maior + 1, "(venda:", maior_venda, ")")

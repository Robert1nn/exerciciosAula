competidores = int(input("Quantos competidores são: "))
papelComprado = int(input("Digite o quanto de papel a escola comprou"))
folhasCompetidor = int(input("Digite o quanto de folhas que cada participante "))

total = competidores * papelComprado

print("O total é: ", total)

if total >= papelComprado:
    print("S")
else:
    print("N")

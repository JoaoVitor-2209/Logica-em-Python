venda = float(input("Digite o valor da venda: "))
if venda > 300:
    desconto = venda * 10 / 100
    venda = venda - desconto
print("Valor da venda com desconto: ", venda)
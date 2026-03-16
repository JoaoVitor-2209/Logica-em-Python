venda = float(input("Digite o valor da venda: "))
if venda >= 1000:
    desconto = venda * 0.05
    venda2 = venda - desconto
else:
    desconto = venda * 0.03
    venda2 = venda - desconto
print(f"O valor antes do desconto era R$ {venda:.2f}, depois do desconto foi {venda2:.2f} ")
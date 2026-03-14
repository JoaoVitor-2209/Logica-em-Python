sal = float(input("Digite o seu salario "))
ir = float
if sal <= 1900:
    ir = 0
elif sal <= 2800:
        ir = sal * 0.15
else:
        ir = sal * 0.275
sal_liq = sal - ir
print("Imposto de renda: ", ir)
print("Salario Liquido: ", sal_liq)

sal = float(input("Digite o seu salario "))
ir = float
if sal <= 2428.80:
    ir = 0
elif sal <= 2826.65:
    ir = sal * 0.075
elif sal <= 3751.05:
    ir = sal * 0.15
elif sal <= 4664.68:
    ir = sal * 0.225
else:
    ir = sal * 0.275

sal_liq = sal - ir
print(f"Imposto de renda: {ir:.2f}")
print(f"Salario Liquido: {sal_liq:.2f}")
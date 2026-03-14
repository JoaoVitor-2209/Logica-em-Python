tc = int(input("Digite o seu tempo de casa: "))
sal = float(input("Digite o seu salario "))
if tc < 3:
    aumento = sal * 0.05
else:
    aumento = sal * 0.1
nv_sal = sal + aumento
print("O seu salario foi de:", sal," para:", nv_sal)


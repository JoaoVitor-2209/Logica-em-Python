# Entrada
valor = int(input("Informe o valor do saque: "))
# Processamento
n100 = valor // 100  # Será armazenado a quantidade de notas de 100
valor = valor % 100  # Resto da Divisão, para descobrir o quanto falta
n50 = valor // 50  # Valor inteiro do quociente da divisão
valor = valor % 50  # Valor inteiro do resto da divisão
n20 = valor // 20
valor = valor % 20
n10 = valor // 10
valor = valor % 10
n5 = valor // 5
valor = valor % 5
n2 = valor // 2
valor = valor % 2
# Saída
print("\nQuantidade de notas:")

if n100 > 0:
    print("Notas de 100:", n100)

if n50 > 0:
    print("Notas de 50:", n50)

if n20 > 0:
    print("Notas de 20:", n20)

if n10 > 0:
    print("Notas de 10:", n10)

if n5 > 0:
    print("Notas de 5:", n5)
if n2 > 0:
    print("Notas de 2:", n2)
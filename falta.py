dia = int(input("Digite a quantidade de dias letivos: "))
falta = int(input("Digite a quantidade de faltas: "))
limite = dia * 0.25
if falta > limite:
    print("Reprovado por faltas")
else:
    print("Ok")

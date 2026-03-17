n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1+n2+n3+n4)/4

dia = int(input("Digite a quantidade de dias letivos: "))
falta = int(input("Digite a quantidade de faltas: "))
limite = dia * 0.25

if (media >= 6 and falta < limite):
    print(f"Aprovado por falta e nota, sua media foi {media:.2f}")
elif (media < 6 and falta > limite):
    print(f"Reprovado por falta e nota, sua media foi {media:.2f}")
elif (media < 6):
    print(f"Reprovado por nota, sua media foi {media:.2f}")
else:
    print(f"Reprovado por falta, sua media foi {media:.2f}")
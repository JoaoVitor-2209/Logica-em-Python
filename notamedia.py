n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1+n2+n3+n4)/4
if media >= 7:
    print(f"Aprovado, sua media foi {media:.2f}")
else:
    print(f"Reprovado, sua media foi {media:.2f}")

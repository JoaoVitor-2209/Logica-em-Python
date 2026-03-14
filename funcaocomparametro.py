def nota_valida(nota):
    if nota >= 0 and nota <=10:
        return True
    else:
        return False

nota1 = float(input("digite a primeira nota: "))
if (nota_valida(nota1)):
    nota2 = float(input("digite a segunda nota: "))
    if (nota_valida(nota2)):
        media = (nota1+nota2) / 2
        print ("a media das notas {0} e {1} é {2}". format(nota1,nota2, media))
    else:
        print("a nota 2 => {nota2} é invalida")
else:
    print("a nota 1 => {nota1} é invalida")
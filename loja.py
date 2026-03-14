##Leia o valor original de um produto.
produt = float(input("Digite o valor do produto: "))
porce = float(input("Digite a porcentagem de desconto: "))
#Calcule o valor correspondente a 15% de desconto.
desc = produt * (porce/100)
#Calcule o valor final do produto após aplicar o desconto.
valorf = produt - desc
#Exiba:
print(f"O valor do produto é {produt}, o valor do desconto é {desc}, e com o desconto o valor fica: {valorf} ")
#O valor original
#O valor do desconto
#O valor final a ser pago pelo cliente
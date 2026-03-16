segundos = int(input("Digite a quantidade de segundos: "))
#Entrada de dados do tipo inteiro
horas = segundos // 3600
#Converte em horas o valor fornecido pelo usuário
segundos = segundos % 3600
#Guarda o resto da divisão
minutos = segundos // 60
#Converte em minutos
segundos = segundos % 60

print(horas,"h", minutos,"m", segundos,"s")
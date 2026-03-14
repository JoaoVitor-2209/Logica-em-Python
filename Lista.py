# lista em python
lista = [2,True,5.2]
#print(lista)

# add dados em lista
lista.append(45)
#print(lista)

# edita dados na lista
lista.insert(0,56)
#print(lista)

#remove ultimo lista
lista.pop()
##print(lista)

# limpar lista
lista.clear
#print(lista)

# preencha 5 elementos na lista
lista = []
for cont in range(0,5,1):
    x = float(input("Digite um elemento: "))
    lista.append(x)
#print(lista)

#for i in range(0,5,1):
#    print(lista[i])

#mostra elem da lista
for elem in lista:
    print(elem)

#soma os elementos da lista
soma = 0
for elem in lista:
    soma += elem
print(soma)
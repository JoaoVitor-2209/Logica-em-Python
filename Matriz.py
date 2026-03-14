matriz = [[0,0],[0,0],[0,0],[0,0]]
print("Preenchendo a Matriz")
for l in range(4):
    for c in range(2):
        matriz[l][c]= int(input(f"Matriz[{l}][{c}]= "))

print("\nExibindo a Matriz...")
for l in range(4):
    for c in range(2):
        print(f"{matriz[l][c]}\t",end=" " )
    print()

soma = 0
for l in range(4):
    for c in range(2):
        soma += matriz[l][c]
print("\nSoma = ",soma)
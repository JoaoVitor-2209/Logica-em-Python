opcao = input("Digite[S]im e [N]ão: ")

while opcao != 's' and opcao != 'S' and opcao != 'n' and opcao != 'N':
    print("Voce digitou", opcao, "Digite S ou N!")
    opcao = input("Digite[S]im e [N]ão: ")

print("Voce digitou", opcao)
def saudacao(hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa Tarde"
    else:
        msg = "Boa Noite"

    print(msg,", Seja Bem-Vindo")

hora = int(input("digite sua hora: "))
saudacao (hora)

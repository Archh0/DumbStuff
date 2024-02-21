import random

Esco = input("Oie! Gostaria de jogar Pedra Papel e Tesoura comigo?\nSim\nNão\n")

if Esco == 'Sim':
    print("Maravilha! Vamos começar!")

    EscosConsole = ['Pedra', 'Papel', 'Tesoura']
    EscoConsole = random.choice(EscosConsole)

    EscoUSER = input("Escolha qual você quer jogar!\nPedra\nPapel\nTesoura\n")

#Aqui começa as possibilidas de escolhas.

    if EscoUSER == 'Pedra' and EscoConsole == 'Tesoura':
        print(f"Você ganhou! Eu escolhi {EscoConsole}!\n:D")

    elif EscoUSER == 'Papel' and EscoConsole == 'Pedra':
        print(f"Você ganhou! Eu escolhi {EscoConsole}!\n:D")

    elif EscoUSER == 'Tesoura' and EscoConsole == 'Pedra':
        print(f"Você ganhou! Eu escolhi {EscoConsole}!\n:D")

    elif EscoUSER == 'Pedra' and EscoConsole == 'Pedra':
        print(f"Empatamos! Eu escolhi {EscoConsole} e você também!\n:D")

    elif EscoUSER == 'Papel' and EscoConsole == 'Papel':
        print(f"Empatamos! Eu escolhi {EscoConsole} e você também! \n:D")

    elif EscoUSER == 'Tesoura' and EscoConsole == 'Tesoura':
        print(f"Empatamos! Eu escolhi {EscoConsole} e você também!\n:D")

    elif EscoUSER == 'Pedra' and EscoConsole == 'Papel':
        print(f"Eu venci! Pois escolhi {EscoConsole} e você {EscoUSER}!")

    elif EscoUSER == 'Papel' and EscoConsole == 'Tesoura':
        print(f"Eu venci! Pois escolhi {EscoConsole} e você {EscoUSER}")

    elif EscoUSER == 'Tesoura' and EscoConsole == 'Pedra':
        print(f"Eu venci! Pois escolhi {EscoConsole} e você {EscoUSER}")

    else:
        print(f"Assim não dá para jogar duuuh! Eu não consigo jogar contra {EscoUSER}!\nHuh!\n")

#Aqui acaba as possibilidas de escolhas.

elif Esco == 'Não':
    print("Tudo bem! :D\nAté mais!")

else:
    print("Não consegui entender a sua resposta, mas fique tranquilo!\nApenas reinicie o programa!")

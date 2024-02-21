# D4, D6, D8, D10, D12, D20
import random
while True:
    Escolha = input("Bem-vindo ao programa! Estamos rodando agora, gostaria de continuar?\n1. Sim\n2. Não\n")
    if Escolha == '1':
        print('Okay vamos lá!')
        print('Primeiramente, eu sou o programa dos DadosRPG mas com loop!\nVamos continuar!')
        print('Sendo um programade DadosRPG eu consigo jogar os seguintes dados para você:')
        print('D4, D6, D8, D10, D12 e o D20')
        print('Escolha um dos abaixo:')
        print('1. D4')
        print('2. D6')
        print('3. D8')
        print('4. D10')
        print('5. D12')
        print('6. 20')
        print('7. Nenhum')
        ListaDADOS = [
            ListaD4 := [0, 1, 2, 3, 4],
            ListaD6 := [0, 1, 3, 4, 5, 6, 7, 8],
            ListaD8 := [0, 1, 2, 3, 4, 5, 6, 7, 8],
            ListaD10 := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            ListaD12 := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            ListaD20 := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        ]
        EscolhaDADOS = input('Qual dado você quer jogar?\n')
        if EscolhaDADOS == '1':
            EscolhaConsole1 = random.choice(ListaD4)
            print(f'O resultado é {EscolhaConsole1}!')
        elif EscolhaDADOS == '2':
            EscolhaConsole2 = random.choice(ListaD6)
            print(f'O resultado é {EscolhaConsole2}!')
        elif EscolhaDADOS == '3':
            EscolhaConsole3 = random.choice(ListaD10)
            print(f'O resultado é {EscolhaConsole3}!')
        elif EscolhaDADOS == '4':
            EscolhaConsole4 = random.choice(ListaD12)
            print(f'O resultado é {EscolhaConosole4}!')
        elif EscolhaDADOS == '5':
            EscolhaConsole5 = random.choice(ListaD20)
            print(f'O resultado é {EscolhaConsole5}!')
        elif EscolhaDADOS == '7':
            print('Okay!')
    elif Escolha == '2':
        print('Okay... Até mais!')
        break
    else:
        print('Infezlimente não entendi!')

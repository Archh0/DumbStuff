import math # Para futuras alterações do código
import random

while True:
    print('Olá, escolha:')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('7. Nenhuma')

    Escolha = input('Escolha que tipo de equação queira gerar\n')
    
    if Escolha == '1':

        print('Okay')
        Num1 = random.randint(-1000000, 1000000)
        Num2 = random.randint(-1000000, 1000000)
        Resposta = float(input(f'Resolva: {Num1} + {Num2}\n'))
        Solucao = Num1 + Num2

        if Resposta == Solucao:
            print(f'Está certo.\nÉ certo que {Num1} + {Num2} é {Resposta}')

        else:
            print('Está errado\nPorém tente novamente!\nCaso não consiga resolver vou lhe ajudar!')
            Resposta2 = input('Tente novamente!\n')

            if Resposta2 == Solucao:
                print('Está certo! Viu só? Você acertou!')

            else:
                print('Está errado... Porém não desanime! Tente outra questão')
                print(f'O resultado era {Solucao}')

    elif Escolha == '2':

        print('Vamos lá!')

        Num1SUB = random.randint(-1000000, 1000000)
        Num2SUB = random.randint(-1000000, 1000000)
        RespostaSUB = float(input(f'Resolva: {Num1SUB} - {Num2SUB}\n'))
        SolucaoSUB = Num1SUB - Num2SUB

        if RespostaSUB == SolucaoSUB:
            print(f'Está certo que {Num1SUB} - {Num2SUB} é {RespostaSUB}')

        else:
            print('Está errado\nPorém tente novamente!\nCaso não consiga vou lhe ajudar!')
            Resposta2SUB = input('Tente novamente!\n')

            if Resposta2SUB == SolucaoSUB:
                print('Está certo! Você conseguiu! Acertou!')

            else:
                print('Está errado... Porém não fique triste! Tente outra questão')
                print(f'A resposta certa era {SolucaoSUB}')

    elif Escolha == '3':

        print('Bora lá!')

        Num1MUL = random.randint(-1000000, 1000000)
        Num2MUL = random.randint(-1000000, 1000000)
        RespostaMUL = float(input(f'Resolva!\nQuanto é {Num1MUL} vezes {Num2MUL}?\n'))
        SolucaoMUL = Num1MUL * Num2MUL

        if RespostaMUL == SolucaoMUL:
            print(f'Está certo que {Num1MUL} vezes {Num2MUL} é {SolucaoMUL}!\nParabéns!')

        else:
            print('Infelizmente está errado!\nNão fique triste você consegue!\nTente novamente!')
            Resposta2MUL = input('Tente outra vez!\n')

            if Resposta2MUL == SolucaoMUL:
                print('Viu só?\nVocê conseguiu! Com esforço, você consegue!')

            else:
                print(f'Me desculpe... Você errou... A resposta era {SolucaoMUL}')

    elif Escolha == '4':

        print('Quer fazer uma equação de divisão? Tudo bem!\nVamos lá!')
        Num1DIV = random.randint(-1000000, 1000000)
        Num2DIV = random.randint(-1000000, 1000000)
        SolucaoDIV = Num1DIV / Num2DIV

        RespostaDIV = float(input(f'Qual o resultado?\n{Num1DIV} dividido por {Num2DIV}?\n'))

        if RespostaDIV == SolucaoDIV:
            print(f'Está certo! É certo que {Num1DIV} dividido por {Num2DIV} é {SolucaoDIV}!\nParabéns!')

        else:
            Resposta2DIV = input('Tente novamente!\n')

            if Resposta2DIV == SolucaoDIV:
                print('Muito bem! Você conseguiu! Viu só!? Você consegue!')

            else:
                print(f'Me desculpa, porém {Num1DIV} dividido por {Num2DIV} não é nem {RespostaDIV}, nem {Resposta2DIV}')
                print(f'Era {SolucaoDIV}... Sorry!')

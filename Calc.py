def add(n1, n2):
    result = n1 + n2
    print(result)

def sub(n1, n2):
    result = n1 - n2
    print(result)

def mul(n1, n2):
    result = n1 * n2
    print(result)

def div(n1, n2):
    if n2 == 0:
        n2 = float(input('Não é possível dividir por zero!\nInsira outro número: '))
    result = n1 / n2
    print(result)


while True:
    
    print('Essa é minha calculadora!\nEscolha alguma das seguintes opções:\n')

    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Mais opções..')
    print('6. Sair\n')
      
    inicio = int(input('Para prosseguir, insira aqui a opção que escolheste:   '))

    if inicio == 6:
        print('Até mais!')
        break

    elif inicio == 1:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        add(n1, n2)

    elif inicio == 2:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        sub(n1, n2)

    elif inicio == 3:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        mul(n1, n2)

    elif inicio == 4:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        div(n1, n2)

    elif inicio == 5:
        print('Eu tenho preguiça, vá embora')
        break

def adi(n1, n2):

    Resultado = n1 + n2
    print(Resultado)

def sub(n1, n2):

    Resultado = n1 - n2
    print(Resultado)

def mul(n1, n2):

    Resultado = n1 * n2
    print(Resultado)

def div(n1, n2):

    if n2 == 0:
        while n2 == 0:
            n2 = float(input("Todo número dividido por zero (0) é zero\nPor isso, insira outro número: "))
        
    else:
        Resultado = n1 / n2
        print(Resultado)

def Inicio():
    print("Slecione uma das possíveis opções:\n")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Saída")


while True:

    Inicio()
    userEscolha = int(input("Por favor, escolha alguma: "))
    
    if userEscolha == 1:
        
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        
        adi(n1, n2)
                
    elif userEscolha == 2:
        
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

        sub(n1, n2)
        
    elif userEscolha == 3:
        
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

        mul(n1, n2)
        
    elif userEscolha == 4:
        
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        
        div(n1, n2)
        
    elif userEscolha == 5:
        break

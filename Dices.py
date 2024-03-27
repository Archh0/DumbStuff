from random import randint

while True:
    print("Escolha um tipo de dado que você queria jogar")
    dchoice = int(input("1. D4.\n2. D6.\n3. D8.\n4. D10.\n5. D12.\n6. D20.\n7. Outro.\nSua escolha: "))

    if dchoice == 7:
        lchoice = int(input("Quantos lados você quer que o seu dado tenha?\nInsira o número aqui: "))
        
        print(f"Ótimo!\nO número de lados será {lchoice}!\nO resultado é...\n{randint(0,lchoice)}!")
        break

    elif dchoice == 6:
        print(f"E o resultado é... {randint(0,20)}!")
        break

    elif dchoice == 5:
        print(f"E o resultado é... {randint(0,12)}!")
        break

    elif dchoice == 4:
        print(f"E o resultado é... {randint(0,10)}!")
        break

    elif dchoice == 3:
        print(f"E o resultado é... {randint(0,8)}!")
        break

    elif dchoice == 2:
        print(f"E o resultado é... {randint(0,6)}!")
        break

    elif dchoice == 1:
        print(f"E o resultado é... {randint(0,4)}!")
        break

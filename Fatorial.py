def fatorial():

    total = 1

    for item in range(user_n, 0, -1):
        total = item * total
    print(total)
     
user_n = int(input('Insira o número que queria que eu o transforme em seu fatorial!\n'))

if user_n > 0:
    fatorial()

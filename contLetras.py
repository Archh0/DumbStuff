from random import randint

randMeta = randint(0,46)
portMeta = 46

tentativa = 0

palavra = input("Programa iniciado, insira a sua palavra e irei contar os caracteres presentes: ")

while palavra.isalpha() == False:
    palavra = input("Erro, não insira espaços na palavra.\nTente novamente: ")

while len(palavra) < randMeta or len(palavra) < portMeta:
    tentativa = tentativa + 1
    palavra = input(f"{tentativa}ª tentativa.\nSua palavra teve {len(palavra)} letras, para sair do loop você deve atingir {randMeta} letras ou {portMeta}.\nInsira a sua palavra: ")

if len(palavra) > randMeta or len(palavra) > portMeta:
    print(f"Na sua {tentativa}ª, você conseguiu!\nCom uma palavra com {len(palavra)} letras!")

salario_M = int(input('Quanto você ganha por mês?\n(Sem casas decimais)\n'))
horas_TM = int(input('E quantas horas você trabalha por mês?\n'))

salario_H = salario_M / horas_TM

print(f'Então você ganha por hora {salario_H}!\n')

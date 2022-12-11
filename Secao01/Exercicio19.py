nome = input('Digite o nome do funcionário: ')
sobrenome = input('Digite o sobrenome do funcionário: ')
salario = float(input('Digite o salário atual do funcionário: '))

aumento1 = salario * 0.1
aumento2 = salario * 0.25
aumento3 = salario * 0.3
aumento4 = salario * 0.5

print(f'O funcionário {nome} {sobrenome} tem o salário atual de R$ {salario:.2f}.')
print(f'Com um aumento de 10%, o salário do funcionário {nome} {sobrenome} passa a ser R$ {salario + aumento1:.2f}.')
print(f'Com um aumento de 25%, o salário do funcionário {nome} {sobrenome} passa a ser R$ {salario + aumento2:.2f}.')
print(f'Com um aumento de 30%, o salário do funcionário {nome} {sobrenome} passa a ser R$ {salario + aumento3:.2f}.')
print(f'Com um aumento de 50%, o salário do funcionário {nome} {sobrenome} passa a ser R$ {salario + aumento4:.2f}.')

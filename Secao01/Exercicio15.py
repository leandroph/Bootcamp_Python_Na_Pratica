from math import hypot

print('-' * 50)
print('Calculadora de hipotenusa de um triângulo')

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa1 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa2 = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do triângulo é {hipotenusa1}')
print(f'A hipotenusa do triângulo é {hipotenusa2}')

print('-' * 50)

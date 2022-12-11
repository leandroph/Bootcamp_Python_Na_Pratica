numero = int(input('Digite um número: '))
soma=0
if numero<0:
    print('O número deve ser positivo.')
else:
    for i in range(numero+1):
        soma+=i
        
    print(f'A soma é: {soma}')    
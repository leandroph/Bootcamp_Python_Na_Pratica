numero = int(input('Digite um número: '))
if numero > 1:
    for k in range(2, numero):  
        if numero % k == 0:  #checar se o número é múltiplo de outro no intervalo [2,numero]
            print(f'O número {numero} não é primo.')
            break
    else:  
        print(f'O número {numero} é primo.')
        
else:
    print(f'O número {numero} não é primo.')
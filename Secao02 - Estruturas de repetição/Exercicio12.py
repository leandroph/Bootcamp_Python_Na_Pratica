numero=0
soma=0
números_digitados=0
while 0<=numero<=10:
    numero=float(input('Digite um número real entre 0-10: '))
    if numero<0 or numero>10:
        print(f'Soma dos números digitados: {soma}')
        print(f'Quantidade de números digitados: {números_digitados}')
        break
    soma+=numero
    números_digitados+=1
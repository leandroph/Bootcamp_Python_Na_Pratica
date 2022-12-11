soma=0
for i in range(1,21):
    numero=float(input(f'Número {i}: '))
    soma+=numero
    if i==20:
        print(f'Soma dos números digitados: {soma} ')
        print(f'Média dos números digitados: {soma/20}')
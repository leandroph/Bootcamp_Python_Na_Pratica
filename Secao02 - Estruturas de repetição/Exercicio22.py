lista=[]
for i in range(1,6):
    num = int(input(f'Número {i}: '))
    if num > 0:
        lista.append(num)
        
    if i == 5:
        for n in lista:
            print(f'O quadrado de {n} é {n ** 2}')
lista=[]
soma_par=0
soma_impar=0
 
while True:
    num=int(input('Digite um número: '))
    if num>0:
        lista.append(num)
    else:
        break
        
#contando a quantidade de pares/ímpares da lista
for num in lista:
    if num%2==0:
        soma_par+=1
    else:
        soma_impar+=1
        
print(f'Quantidade de números pares: {soma_par}')
print(f'Quantidade de números ímpares: {soma_impar}')
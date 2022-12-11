lista=[]
x=1
#armazenando os números em uma lista
while len(lista)<20:
    if x%5==0:
        lista.append(x)
        x+=1
    x+=1
 
#mostrando os números na tela
for num in lista:
    print(num)
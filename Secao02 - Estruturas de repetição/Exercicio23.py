num = int(input('Digite um número inteiro positivo: '))
soma = 0  #variável para acumular a soma de todos os inteiros
soma_par = 0  #variável para acumular a soma de todos os pares
soma_impar = 0 #variável para acumular a soma de todos os ímpares
 
if num > 0:  #caso o número digitado seja positivo o programa será executado
    for i in range(1,num+1):
        soma += i  #a cada laço acumulamos cada valor i na nossa variável soma
        if i % 2 == 0:  #caso o número i seja par iremos acumular esse valor
            soma_par += i  #podemos escrever: soma_par=soma_par+i
        if i % 2 != 0:  #a cada laço acumulamos cada valor i na nossa variável soma
            soma_impar += i  #podemos escrever: soma_par=soma_impar+i
            
        if i == num:  
            print(f'Soma total: {soma}')
            print(f'Soma dos números pares: {soma_par}')
            print(f'Soma dos números ímpares: {soma_impar}')
else:  #mensagem caso o número seja negativo ou nulo
    print('O valor inserido não é válido.')
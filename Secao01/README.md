# Exercícios - Seção 01

## Exercício 1:

Escreva um programa que mostre a mensagem 'Hello World!' na tela.

## Exercício 2:

Faça um programa que solicite um número do usuário e apresente a seguinte mensagem na tela:

```python
"O número digitado foi [número]."
```

## Exercício 3

Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.

## Exercício 4

Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.

## Exercício 5
Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:

```python
"A média das notas [nota1] e [nota2] é [média]"
```

## Exercício 6

Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.

## Exercício 7

Faça um programa que peça 5 números de ponto flutuante do usuário e apresente no final a média dos números digitados.

## Exercício 8

Escreva um programa que faça a conversão de um dado valor de metro para quilômetro.

## Exercício 9
Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.

```python
Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.
Dica: você pode usar a biblioteca math para pegar a constante pi.
```

## Exercício 10

Faça um programa que peça uma temperatura em Fahrenheit (F) e converta esta temperatura para grau Celsius (C), mostrando o resultado da conversão na tela.

```python
Use a fórmula: C = 5 * ((F-32) / 9).
```

## Exercício 11

Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:

```python
"[número1]x[número2]=[multiplicação]"

"[número1]/[número2]=[divisão]"
```

## Exercício 12
Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:

```python
"Seja bem-vindo [nome] [sobrenome]."
"Você possui [idade] anos de idade."
```
OBS:
No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato titlecased (capitaliza a string).

## Exercício 13

Escreva um programa que peça um número do usuário via método input e converta esse número para o formato float.

## Exercício 14
Escreva um programa que peça o nome e a idade do usuário. Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem: 

```python
"Seja bem-vindo ao nosso site [nome]!"
```
Caso contrário, apresente a seguinte mensagem: 
```python
"Você não pode acessar nosso site [nome]."
```

## Exercício 15

Elabore um programa para calcular a hipotenusa de um triângulo.

Dicas:

- Veja o módulo math (math.hypot);

- Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

## Exercício 16

Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.

Dica: 

- Utilize o módulo math do Python, especificamente math.fatorial.

## Exercício 17

Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.

Dica: 

- utilize o módulo math.

## Exercício 18

Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

## Exercício 19

Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir o seguinte padrão:

```python
"Olá, [nome] [sobrenome]"

"Seu salário atual é : [salário]"

"Seu salário com 10% de aumento é: [salário]"

"Seu salário com 25% de aumento é: [salário]"

"Seu salário com 30% de aumento é: [salário]"

"Seu salário com 50% de aumento é: [salário]"
```

No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e após a string, enquanto que o último permite colocar a string no formato titlecased (capitaliza string).

## Exercício 20

Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

## Exercício 21

Faça um programa que solicite um número inteiro e mostre o seu valor absoluto.

Dica: 

- Use a função built-in abs().

## Exercício 22

Faça um programa que peça uma string ao usuário e mostre na tela a quantidade de caracteres.

Dica: 

- Use a função built-in len() e trate a string com o método strip().

## Exercício 23

Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:

```python
"O número [número] é [par/ímpar]"
```

## Exercício 24

O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.

```python
IMC<17 - Muito abaixo do peso ideal

17<=IMC<18,5 - Abaixo do peso

18,5<=IMC<25 - Peso normal

25<=IMC<30 - Acima do peso

30<=IMC<35 - Obesidade I

35<=IMC<40 - Obesidade II (severa)

IMC>=40 - Obesidade III (mórbida)
```

## Exercício 25

Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o 
usuário digitar dois números iguais.

## Exercício 26

Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

## Exercício 27

Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

## Exercício 28

Escreva um programa que gere um número aleatório entre 1 e 100 e mostre na tela.

Dica: 
- utilize o módulo random.

## Exercício 29
Elabore um progama para verificar se um ano é bissexto ou não. A condição para ser um ano bissexto é: o ano deve ser divisível por 400; 
ou se for divisível por 4 e não for divisível por 100.

## Exercício 30

Elabore um programa para calcular o tamanho de uma string.

## Exercício 31

Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.

```python
1 | 12/06/2020 - 14:34:17
```

## Exercício 32

Escreva um programa que inverta uma string. Exemplos:

```python
1 | Hello World!
2 | Python
3 | !dlroW olleH
4 | nohtyP
```

## Exercício 33

Escreva um programa para mostrar na tela o calendário do mês de dezembro de 2020. Exemplo:

```python
1 |    December 2020
2 | Mo Tu We Th Fr Sa Su
3 |     1  2  3  4  5  6
4 |  7  8  9 10 11 12 13
5 | 14 15 16 17 18 19 20
6 | 21 22 23 24 25 26 27
7 | 28 29 30 31
```

Dica: 
- importe o módulo calendar.

## Exercício 34

Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

## Exercício 35
Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.  
Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida (número entre 1 e 10) mostre na tela uma mensagem personalizada.

```python
 1 | Exemplo: preço x categoria
 2 | * Categoria 1 - $ 0,5 
 3 | * Categoria 2 - $ 11,3
 4 | * Categoria 3 - $ 17,5
 5 | * Categoria 4 - $ 33,97
 6 | * Categoria 5 - $ 103,47
 7 | * Categoria 6 - $ 44,67
 8 | * Categoria 7 - $ 12,55
 9 | * Categoria 8 - $ 14,87
10 | * Categoria 9 - $ 98,12
11 | * Categoria 10 - $ 131,4
```

## Exercício 36

Resolva o exercício anterior para as categorias de 1 a 8. Utilize estruturas aninhadas.

## Exercício 37

Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e implemente sua solução.
Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.

## Exercício 38

Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:

- Triângulo equilátero: todos os lados possuem o mesmo tamanho;

- Trângulo escaleno: todos os lados possuem medidas diferentes;

- Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

## Exercício 39
Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir dois valores. Caso, o usuário escolha divisão e insira o valor do denominar 0 mostre uma mensagem personalizada. Para os demais casos, mostre na tela o resultado da operação desejada.




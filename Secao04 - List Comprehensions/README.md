# Exercícios - Seção 04

## Exercício 1:

Utilize Compreensão em Lista (List Comprehensions) para criar a lista a seguir.

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Exercício 2

Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Observe que esses números são obtidos através do quadrado de cada número no intervalo [0,9].

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Exercício 3

Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Observe que esses números são obtidos através da raiz quadrada de cada número no intervalo [1,50]. Utilize round() para arredondar as casas decimais.

```
[1.0, 1.41, 1.73, 2.0, 2.24, 2.45, 2.65, 2.83, 3.0, 3.16, 3.32, 3.46, 3.61, 3.74, 3.87, 4.0, 4.12, 4.24, 4.36, 4.47, 4.58, 4.69, 4.8, 4.9, 5.0, 5.1, 5.2, 5.29, 5.39, 5.48, 5.57, 5.66, 5.74, 5.83, 5.92, 6.0, 6.08, 6.16, 6.24, 6.32, 6.4, 6.48, 6.56, 6.63, 6.71, 6.78, 6.86, 6.93, 7.0, 7.07]
```

## Exercício 4

Utilize Compreensão em Lista (List Comprehensions) para criar as listas a seguir.

- a)
```
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
```

- b)
```
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]
```
 
## Exercício 5
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.

```
[1, 3, 5, 7, 9]
```

## Exercício 6

Utilize Compreensão em Lista (List Comprehensions) para criar as listas a seguir.

Lembre que:
```python
[f(x) for x in sequence if condition]
[f(x) if condition else g(x) for x in sequence]
```

- a)
```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
```

- b)
```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
```

## Exercício 7

Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Condição: eleve o número ao quadrado se for par; se o número for ímpar calcule a raiz quadrada - utilize round() para arredondar as casas decimais.

```
[1.0, 4, 1.73, 16, 2.24, 36, 2.65, 64, 3.0, 100, 3.32, 144, 3.61, 196, 3.87, 256, 4.12, 324, 4.36, 400, 4.58, 484, 4.8, 576, 5.0, 676, 5.2, 784, 5.39, 900, 5.57, 1024, 5.74, 1156, 5.92, 1296, 6.08, 1444, 6.24, 1600, 6.4, 1764, 6.56, 1936, 6.71, 2116, 6.86, 2304, 7.0, 2500]
```

Lembre que:

```python
[f(x) for x in sequence if condition]
[f(x) if condition else g(x) for x in sequence]
```

## Exercício 8

Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Ademais, tente resolver este problema sem usar Compreensão em Lista.

```
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

## Exercício 9

A partir das listas

```python
linguagens=['php','JavaScript']
frases=['Eu amo ','Eu odeio ']
```

Use List Comprehension e obtenha a seguinte lista:

```python
['Eu amo php !', 'Eu odeio php !', 'Eu amo JavaScript !', 'Eu odeio JavaScript !']
```

Por fim, tente implementar uma solução sem List Comprehension.

## Exercício 10

A partir da lista

```python
lista=[3, -31, -70, -55, 1, -76, -15, -14, -75, -53, 42, 12, -27, -92, -83, -9, 6, 9, -46, -48, -17, -69, 15, -1, 9, 6, -89, -36, 15, -24, 49, -31, -25, -71, 43, 20, -67, 18, -3, 8, -60, -73, 22, -52, 5, -15, 48, 21, -23, 6, 0]
```

Use List Comprehension e obtenha:
```python
[3, 1, 42, 12, 6, 9, 15, 9, 6, 15, 49, 43, 20, 18, 8, 22, 5, 48, 21, 6, 0]
```

## Exercício 11

A partir da lista

```python
lista=[3, -31, -70, -55, 1, -76, -15, -14, -75, -53, 42, 12, -27, -92, -83, -9, 6, 9, -46, -48, -17, -69, 15, -1, 9, 6, -89, -36, 15, -24, 49, -31, -25, -71, 43, 20, -67, 18, -3, 8, -60, -73, 22, -52, 5, -15, 48, 21, -23, 6, 0]
```

Use List Comprehension e obtenha:

```python
[3, 31, 70, 55, 1, 76, 15, 14, 75, 53, 42, 12, 27, 92, 83, 9, 6, 9, 46, 48, 17, 69, 15, 1, 9, 6, 89, 36, 15, 24, 49, 31, 25, 71, 43, 20, 67, 18, 3, 8, 60, 73, 22, 52, 5, 15, 48, 21, 23, 6, 0]
```

## Exercício 12

A partir da lista

```python
frutas=['  BaNanA    ', '  morangO ', ' mAçã  ','   MeLão']
```

Use List Comprehension e obtenha as seguintes listas:

```python
['Eu gosto de Banana !', 'Eu gosto de Morango !', 'Eu gosto de Maçã !', 'Eu gosto de Melão !']
['BANANA', 'MORANGO', 'MAÇÃ', 'MELÃO']
['banana', 'morango', 'maçã', 'melão']
```

## Exercício 13

Utilize Compreensão em Lista (List Comprehension) para criar as listas a seguir.



- a)
```
[(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7), (13, 8), (14, 9)]
```

- b)
```
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
```

## Exercício 14

A partir da lista

```python
matriz=[[1,2,3], [4,5,6], [7,8,9]]
```

Use List Comprehension e obtenha:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Na sequência utilize a função sum() para obter a soma destes números.

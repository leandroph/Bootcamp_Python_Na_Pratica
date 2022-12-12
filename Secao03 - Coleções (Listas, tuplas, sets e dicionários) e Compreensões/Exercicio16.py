tupla1 = ('A','B','A','Z','Z','X','A','E','K','G','H')

# mostre na tela o tamanho desta tupla;
tamanho = len(tupla1)
print(f'Tamanho da tupla: {tamanho}')

# ordene a tupla e mostre o resultado na tela;
tupla_ordenada = sorted(tupla1)
print(f'Tupla ordenada: {tupla_ordenada}')

# mostre na tela o número de ocorrências da string 'A';
print(f'Número de ocorrências da string "A": {tupla1.count("A")}')

# mostre na tela o número de ocorrências da string 'B';
print(f'Número de ocorrências da string "B": {tupla1.count("B")}')

# mostre na tela o índice da string 'X';
print(f'Índice da string "X": {tupla1.index("X")}')

# mostre na tela o último elemento da tupla1.
print(f'Último elemento da tupla1: {tupla1[-1]}')
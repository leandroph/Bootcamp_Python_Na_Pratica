# Crie um script para iterar no dicionário abaixo e mostrar na tela todas as suas chaves, uma a uma.

produto1={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}

for chave in produto1:
    print(chave)

print()
# Crie um script para iterar no dicionário produto1 e mostrar na tela todos os seus valores, um a um.

for valor in produto1.values():
    print(valor)

print()
# Crie um script para iterar no dicionário produto1 e mostrar chave,valor na tela.

for chave, valor in produto1.items():
    print(f'{chave}: {valor}')
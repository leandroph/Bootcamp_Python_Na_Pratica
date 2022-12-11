# primeira solução
for num in range(1, 201, 2):
    print(num, end=' ')

print('\n')

# segunda solução
for num in range(1, 201):
    if num % 2 != 0:
        print(num, end=' ')
x = 1

for i in range(1, 11):
    print(i)
    if i == 10:
        while x <= 10:
            print(x)
            x += 1
            if x == 11:
                y = 1
                while y <= 10:
                    print(y)
                    y += 1
                    if y == 11:
                        print('Fim')

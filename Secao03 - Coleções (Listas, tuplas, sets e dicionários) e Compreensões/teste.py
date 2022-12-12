from statistics import median,mode,multimode,variance,stdev
 
lista=[-1505, 2518, 2333, 4682, -1740, 1067, 995,22,2,
       -1153, -4098, 4560, 2958, 3640, -4154, 2345,4, 
       -1601, 158, -4044, -98, 707, 359, -3088, 527, 
       -3004, -4045, 563, -4137, 4598, -3862, 488, -1, 
       3445, 3820, 504, -1475, 1626, -1252, 2059, 16, 
       -1472, 2610, -4643, 2912, -2517, -4604, -1476, 
       3950, -4640, -229, 229, -3452, 4309, 2356, 66, 
       3728, -1846, -635, -3581, 4457, -2592, -1066,4,
       -1006, -164, 805, -4500, -455, 2245, -4959,2, 
       -2415, 2038, 4512, 1243, 349, -1153, 3623, 631, 
       2209, -3349, -2417, 4429, -1324, -4101, -1354, 
       4400, -4968, -4433, 2042, 904, 932, 1331, 4955, 
       -3775, -333, 1012, 2192, -161, -224, 1505, -1615, 
       -2165, 3666, -4253, -358, -3939, -2641, 1228, 
       -608, -2280, 4939, -3355, 1340, -57, 3346, 2686, 
       -1572, 1991, -2351, -3972, -1683, -1509, -2488, 
       266, -2991, -795, -4032, 2397, 2391, 3654, -1044, 
       -2204, -2440, -1280, 2714, -4151, -1951, 3684, 
       -4251, 3748, -4359, -1436, -2190, 4538, -3563, 
       1542, 1926, -3940, -2274, -4223, 2504, -4112, 2388,
]
 
 
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')
print(f'Soma de todos os elementos da lista: {sum(lista)}')
print(f'Quantidade de elementos da lista: {len(lista)}')
print(f'Média aritmética: {sum(lista)/len(lista):.2f}')
print(f'Moda: {multimode(lista)}')
print(f'Mediana: {median(lista)}')
print(f'Variância: {variance(lista):.2f}')
print(f'Desvio padrão: {stdev(lista):.2f}')

'''
1 | Maior número: 4955
2 | Menor número: -4968
3 | Soma de todos os elementos da lista: -38259
4 | Quantidade de elementos da lista: 155
5 | Média aritmética: -246.83
6 | Moda: [2, -1153, 4]
7 | Mediana: -161
8 | Variância: 7629024.95
9 | Desvio padrão: 2762.07
'''
from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = randint(1, 10)   # input(f'Insira um valor para [{i}][{j}]: ')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:-^7}]', end=' ')
    print()

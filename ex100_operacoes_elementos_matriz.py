matriz = [[], [], []]
soma_pares = soma_col3 = maior_seg = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Insira um número para [{linha}][{coluna}]: ')))
        # soma de todos os valores pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        # soma da terceira coluna
        if coluna == 2:
            soma_col3 += matriz[linha][coluna]
        # maior valor da segunda linha
        if linha == 1:
            if matriz[linha][coluna] > maior_seg:
                maior_seg = matriz[linha][coluna]

print('\nSua matriz é:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:-^7}]', end=' ')
    print()

print(f'\nSoma dos pares: {soma_pares};\nSoma dos valor da terceira coluna: {soma_col3};\nMaior valor da segunda linha: {maior_seg}.')

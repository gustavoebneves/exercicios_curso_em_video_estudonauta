num = [[], []]
for numeros in range(7):
    n = int(input(f'Insira o {numeros+1}º número : '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()
print(f'\nLista completa: {num}.\nNúmeros Pares inseridos: {num[0]}.\nNúmeros Ímpares inseridos: {num[1]}.')

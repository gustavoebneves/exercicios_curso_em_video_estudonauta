val = ((int(input('Insira um número: '))),
       (int(input('Insira outro número: '))),
       (int(input('Insira mais um número: '))),
       (int(input('Insira o último número: '))))
print(f'O valor 9 apareceu {val.count(9)} vezes na tupla.')
if 3 in val:
    print(f'O valor 3 apareceu pela primeira vez na {val.index(3) + 1}ª posição.')
else:
    print('O valor 3 não apareceu na tupla.')
pares = []
for num in range(0, len(val)):
    if val[num] % 2 == 0:
        pares.append(val[num])
print(f'Os números pares encontrados na tupla foram: {pares}.')

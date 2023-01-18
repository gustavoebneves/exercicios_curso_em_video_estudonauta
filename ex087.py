itens = ('Pão', 1, 'Açúcar', 1000, 'Arroz', 100, 'Feijão', 20)
print('--' * 15)
print('{:^30}'.format('Listagem de preços'))
print('--' * 15)
print(f'''{itens[0]}.......R$ {itens[1]}
{itens[2]}....R$ {itens[3]}
{itens[4]}.....R$ {itens[5]}
{itens[6]}....R$ {itens[7]}''')
print('--' * 15)

# OU...
print('\n')
print('--' * 15)
print('{:^30}'.format('Listagem de preços'))
print('--' * 15)

for num in range(0, len(itens)):
    if num % 2 == 0:
        print(f'{itens[num]:.<15} R$ ', end='')
    if num % 2 != 0:
        print(f'{itens[num]:>7.2f}')


print('--' * 15)

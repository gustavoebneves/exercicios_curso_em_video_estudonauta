from math import factorial
ct = fat = n = int(input('Insira um número: '))
fat2 = 1
while ct != 1:
    ct = ct - 1
    fat = fat * ct
print(f'\nWhile:\nO fatorial de {n} é igual a: {fat}')

for h in range(n, 1, -1):
    fat2 = fat2 * h
print(f'\nFor:\nO fatorial de {n} é igual a: {fat2}')

# OU

print('\nBiblioteca/Modulo math:')
print('O fatorial de {} é igual a: {}.'.format(n, factorial(n)))

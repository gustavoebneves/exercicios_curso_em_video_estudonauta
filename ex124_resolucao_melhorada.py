'''
Adapte o código do desafio #123, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''

import ex123_moeda
help(ex123_moeda.aumentar)
help(ex123_moeda.dobrar)
help(ex123_moeda.diminuir)
help(ex123_moeda.metade)
help(ex123_moeda.moeda)

print('__'*80)
print('\nINÍCIO DO PROGRAMA')
print('¨'*18)

money = float(input('Insira o valor R$ '))

print(f'Seu dinheiro com aumento ficou em {ex123_moeda.aumentar(money, True)}')
print(f'Seu dinheiro com diminuição ficou em {ex123_moeda.diminuir(money, True)}')
print(f'O dobro dos seus {ex123_moeda.moeda(money)} é igual a {ex123_moeda.dobrar(money, True)}')
print(f'A metade dos seus {ex123_moeda.moeda(money)} é igual a {ex123_moeda.metade(money, True)}')

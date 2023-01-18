from ex123_moeda import aumentar, dobrar, diminuir, metade
help(aumentar)
help(dobrar)
help(diminuir)
help(metade)

print('__'*80)
print('\nINÍCIO DO PROGRAMA')
print('¨'*18)

money = float(input('Insira o valor R$ '))
print(f'Seu dinheiro com aumento ficou em R$ {aumentar(money)}')
print(f'Seu dinheiro com diminuição ficou em R$ {diminuir(money)}')
print(f'O dobro dos seus {money} reais é igual a {dobrar(money)}')
print(f'A metade dos seus {money} reais é igual a {metade(money)}')

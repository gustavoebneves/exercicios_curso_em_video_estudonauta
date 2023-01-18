from random import randint
maior = menor = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for numero in tupla:
    print(numero, end=' ')

for ct in range(0, len(tupla)):
    if ct == 0:
        maior = tupla[ct]
        menor = tupla[ct]
    else:
        if tupla[ct] > maior:
            maior = tupla[ct]
        if tupla[ct] < menor:
            menor = tupla[ct]

print(f'\nO menor valor sorteado foi {menor}.\nO maior valor sorteado foi {maior}.')


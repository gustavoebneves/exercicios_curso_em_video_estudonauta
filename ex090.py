numeros = []
maior = menor = 0
for ct in range(0, 5):
    numeros.append(int(input(f'Insira o {ct}º número: ')))
    if ct == 0:
        maior = menor = numeros[ct]
    else:
        if numeros[ct] < menor:
            menor = numeros[ct]
        if numeros[ct] > maior:
            maior = numeros[ct]
print(f'Sua lista é: {numeros}.')

print(f'O menor valor inserido foi: {menor}; Ele apareceu nas posições: ', end='')
# indice é o índice do valor
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice}...', end='')

print(f'\nO maior valor inserido foi: {maior}; Ele apareceu nas posições: ', end='')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice}...', end='')
print('\n')

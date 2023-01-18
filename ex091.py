lista = []
num = ''
while num != 999:
    num = int(input('Insira um número (999 para parar): '))
    if num not in lista:
        lista.append(num)
    elif num == 999:
        print('Tudo bem.')
    else:
        print('Valor duplicado. Não irei adicioná-lo!')
lista.pop()
lista.sort()
print(f'Sua lista somente com números diferentes uns dos outros é: {lista}.')

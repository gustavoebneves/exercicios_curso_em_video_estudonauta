lista = []
num = ''
while num != 999:
    num = int(input('Insira um número (999 para parar): '))
    lista.append(num)
lista.pop()
lista.sort()
lista.reverse()  # ou lista.sort(reverse=True)
print(f'Você digitou {len(lista)} números.\nLista decrescente: {lista}.')
if 5 in lista:
    print('O número 5 foi inserido.')
else:
    print('O número 5 não foi inserido.')

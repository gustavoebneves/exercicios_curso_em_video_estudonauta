n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira, novamente, outro número: '))
lista = [n1, n2, n3]
lista.sort()
print(lista)
print('Solução em lista\nO maior valor é: {}\nO menor valor é: {}'.format(max(lista), min(lista)))
print('\nSolução com condicionais')

if n1 > n2 and n1 > n3:
    print('O maior valor é: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior valor é: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior valor é: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor é: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor valor é: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor valor é: {}'.format(n3))

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira, novamente, outro número: '))

soma = n1 + n2

if soma > n3:
    print('A soma entre {} e {} é maior que {}'.format(n1, n2, n3))
elif soma == n3:
    print('{} e {} são iguais'.format(soma, n3))
else:
    print('{} é maior que a soma entre {} e {}'.format(n3, n1, n2))
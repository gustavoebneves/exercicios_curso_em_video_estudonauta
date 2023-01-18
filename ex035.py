while True:
    n = int(input('Insira um número para saber se ele é par: '))

    if n % 2 == 0:
        print('{} é par!'.format(n))
    else:
        print('{} é ímpar!'.format(n))

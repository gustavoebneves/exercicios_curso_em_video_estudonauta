while True:
    n = int(input('Insira um número: '))
    ct = 1
    divisores = 0
    for i in range(n):
        if n % ct == 0:
            divisores += 1
        ct += 1
    if divisores == 2:
        print('{} é primo\n'.format(n))
    else:
        print('{} não é primo\n'.format(n))


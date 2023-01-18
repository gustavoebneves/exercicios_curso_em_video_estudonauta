while True:
    ct = n = 0
    n = int(input('\nInsira um número: '))
    if n < 0:
        break
    while ct < 10:
        ct += 1
        print(f'{n} x {ct} = {n*ct}')
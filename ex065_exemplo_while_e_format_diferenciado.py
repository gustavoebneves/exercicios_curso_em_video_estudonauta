for c in range(1, 11):
    print(c)
print('Fim\n')

# quando se sabe o fim do loop, melhor usar for

ct = 1
while ct != 10:
    print(c)
    ct += 1
print('Fim')
n = 1
imp = par = 0
while n != 0:
    n = int(input('Insira um número: '))
    if n % 2 == 0 and n != 0:
        par += 1
    elif n % 2 != 0 and n != 0:
        imp += 1
print(f'Você digitou {par+1} números pares e {imp} números impares.')

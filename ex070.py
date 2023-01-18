print('-=-'*8)
print('{:^24}'.format('Gerador de PA'))
print('-=-'*8)
n1 = int(input('\nInsira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
n11 = n1 - 1
n12 = n1
nt = 0

print('\nWhile:')
print('(', end='')
while nt != 10:
    nt += 1
    n11 = n11 + r
    print(n11, end=' - ')
print(')')

print('\nFor:')
print('(', end='')
for i in range(1, 11):
    print(n12, end=' - ')
    n12 += r
print(')')
print('\nAcabou')

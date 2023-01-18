for c in range(0, 3):
    print('Oi')
print('Fim\n')

for c in range(3, 0, -1):
    print('Oi')
print('Fim\n')

for c in range(0, 6, 2):
    print('Oi')
print('Fim\n')

n = int(input('Digite um número: '))
for c in range(0, n):
    print('Oi')
print('Fim\n')

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))  # passo não pode ser 0
for c in range(inicio, fim, passo):
    print('Oi')
print('Fim\n')

s = 0
for c in range(0, 3):
    n = int(input('Insira um número: '))
    s += n
print('Somatório = {}'.format(s))

n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
for i in range(1, 11):
    print(n1, end=' - ')
    n1 += r
print('Acabou')

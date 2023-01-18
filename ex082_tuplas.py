lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Patata frita')
print(lanche)
print('--'*17)
for comida in lanche:
    print(f'Vou comer {comida}.')

print('--'*17)

for ct in range(0, len(lanche)):  # quando precisar da posição
    print(f'Vou comer {lanche[ct]}. Posição: {ct};')

print('--' * 17)

for posicao, comida in enumerate(lanche):  # quando precisar da posição
    print(f'Vou comer {comida}. Posição: {posicao};')

print('--'*17)
print('Comi afuzel\n')

print('\n'+lanche[2])
print(lanche[-2])
print(lanche[0:3])
print(lanche[3:])
print(lanche[1:3])

print(sorted(lanche))  # Ordem alfabética. Mudou momentaneamente.
print(lanche, '\n')
# print(f'Enumerate lanche: {enumerate(lanche)}')   sei la

a = (1, 2, 3, 4)
b = (5, 6, 7, 8, 9, 10)
c = a + b
d = b + a
print(c)
print(d)
print(f'Quantas vezes 5 aparece em C: {c.count(5)}')
print(f'Índice do número 8 em C: {c.index(8)}')  # se tiver mais de uma ocorrência, usar: c.index(9, 3)
                                                                # vai dizer o índice do 9 a partir da terceira posição
print('\n')
a = ('oi', 'tudo')
b = 'bem', 'com', 'você', '?'  # tupla não precisa de parenteses
c = a + b
d = b + a
print(c)
# del(d) apaga d da memória e da erro se tentar utilizar
print(d)

lista = []
impares = []
pares = []
num = ''
while num != 999:
    num = int(input('Insira um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
lista.pop()
impares.pop()
print(f'Você inseriu os seguintes números: {lista}.')
print(f'{pares} são os números pares que você inseriu.')
print(f'{impares} são os números ímpares que você inseriu.')

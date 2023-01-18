frase = str(input('Insira uma frase: ')).strip().lower().replace(' ', '').replace(',', '')
frase_inversa = ''

for letra in range(len(frase) - 1, -1, -1):
    frase_inversa += frase[letra]
print('\nFrase inserida normalzona: {}\nFrase inserida invertida : {}'.format(frase, frase_inversa))

if frase == frase_inversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

#  OU

frase_inversa2 = frase[::-1]
print('\nFrase inserida normalzona: {}\nFrase inserida invertida : {}'.format(frase, frase_inversa2))

if frase == frase_inversa2:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
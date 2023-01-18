lista_de_palavras = ('gustavo', 'camila', 'arlindo', 'sebastiao')

for palavra in lista_de_palavras:
    print(f'Na palavra {palavra} tem as vogais:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n')

# Ola, babaca!
frase = str(input('Insira uma frase: ')).strip().lower()
print(frase)
print('A letra a aparece {} vezes na sua frase.'.format(frase.count('a')))
print('A posição em que a letra a aparece pela primeira vez é: {}.'.format(frase.find('a') + 1))
print('A posição em que a letra a aparece pela última vez é: {}.'.format(frase.rfind('a') + 1))
                                                     # rfind procura da direita pra esquerda

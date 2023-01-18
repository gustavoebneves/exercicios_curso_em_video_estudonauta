# Gustavo Eliael Bonow Neves
nome = str(input('Insira seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print('O seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(primeiro_nome[0])))


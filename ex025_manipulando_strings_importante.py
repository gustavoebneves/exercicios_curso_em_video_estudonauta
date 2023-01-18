frase = 'olá, mundo!'
       # 012345678910
       # em Python, toda string é entendida como uma lista, então cada caractere possui um índice
print(frase[0:3])  # imprime do 0 até o 2
print(frase[0:11:2])  # 2 em 2
print(frase[:4])  # começa do 0 até a letra na posição <3>
print(frase[5:])  # imprime tudo a partir do caractere 5
print(frase[5::2])  # imprime tudo a partir do caractere 5 de 2 em 2
print(frase[::-1])  # imprime a frase invertida
print(len(frase))  # mostra o número de caracteres
print(frase.count('o'))  # mostra quantas vezes 'o' aparece na string
print(frase.count('o', 0, 9))  # mostra quantas vezes 'o' aparece na string da posição 0 até a 8
print(frase.find('mundo'))  # mostra a partir de qual posição começa o trecho da string
sei_la = frase.find('ouro')  # se o trecho de string não existir na string selecionada, aparece o valor -1
print(sei_la)
print('ouro' in frase)  # false caso não exista o trecho de string na string
print('mundo' in frase)  # true caso exista o trecho de string na string
print(frase.replace('mundo', 'bicho'))  # frase continua com 'olá, mundo!', mas 'mundo' foi trocado momentaneamente
print(frase.upper())  # muda momentaneamente a frase para toda maiúscula
print(frase.upper().count('O'))  # também é possivel utilizar várias funções juntas
print(frase.lower())  # muda momentaneamente a frase para toda minúscula
print(frase.capitalize())  # deixa a primeira letra maiúscula
print(frase.title())  # deixa maiúscula todas as primeiras letras de lista_de_palavras

frase = '   Aprenda Python  '
print(frase.strip())  # remove os espaços antes ou depois da string
print(frase.rstrip())  # remove os espaços somente depois da string
print(frase.lstrip())  # remove os espaços somente antes da string
print(frase.split())  # separa em lista_de_palavras uma string https://www.w3schools.com/python/ref_string_split.asp
print(frase.split()[0], frase.split()[1])
print(frase.split()[1][0])  # mostra a primeira letra da segunda palavra
# split transforma lista_de_palavras em conteúdos de lista, é possível imprimir um ou mais conteúdos (índice)
frase = frase.strip()
frase = frase.split()
print(', '.join(frase))  # junta lista_de_palavras e as transforma em uma string (pode mudar o separador)

print('''\nTexto é uma manifestação da linguagem, 
uma mensagem usada para transmitir informação 
de um autor para um leitor. Um texto é uma 
manifestação da linguagem. Pode ser definido 
como tudo aquilo que é dito por um emissor e 
interpretado por um receptor. Dessa forma, 
tudo que é interpretável é um texto.''')
# usar aspas triplas para imprimir um texto que está em duas ou mais linhas

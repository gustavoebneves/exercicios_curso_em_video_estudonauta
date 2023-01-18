# cores em python padrão ANSI
# \033[0;33;44m
# o que é cada coisa?
# \ -> padrão
# 33 -> padrão
# [ -> padrão
# 0 -> style/estilo de texto
# ; -> padrão
# 33 -> text_speech/cor do texto
# ; -> padrão
# 44 -> back/fundo do texto
# m -> padrão
#
# Códigos de style:
# 0 -> none/normal
# 1 -> bold/negrito
# 4 -> underline/sublinhado
# 7 -> negative/negativo
#
# Códigos de text_speech:
# 30 -> branco
# 31 -> vermelho
# 32 -> verde
# 33 -> amarelo
# 34 -> azul
# 35 -> roxo
# 36 -> ciano
# 37 -> cinza
#
# Códigos de back:
# 40 -> branco
# 41 -> vermelho
# 42 -> verde
# 43 -> amarelo
# 44 -> azul
# 45 -> roxo
# 46 -> ciano
# 47 -> cinza
# testes
print('Testes')
print('\033[44mOlá, Mundo!')
print('\033[1;44mOlá, Mundo!')
print('\033[1;31;44mOlá, Mundo!')
print('\033[1;31;44mOlá, Mundo!\033[m')
print('\033[1;31mOlá, Mundo!\033[m')
print('\033[7;30;40mOlá, Mundo!\033[m')
print('\033[7;31;40mOlá, Mundo!\033[m')
print('\033[4;31mOlá, Mundo!\033[m')
print('\033[7;30;47mOlá, Mundo!\033[m')
a = 1
b = 2
nome = 'Gustavo'
print('Seu nome é {}{}{}!'.format('\033[4;32m', nome, '\033[m'))
cores = {'limpa':'\033[m', 'verm':'\033[31m', 'verde':'\033[32m'''}
print('Os valores a e b são respectivamente \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('Os valores a e b são respectivamente {}{}{} e {}{}{}!!!'.format(cores['verde'], a, cores['limpa'], cores['verm'], b, cores['limpa']))

# def input_int(mensagem):
#     while True:
#         try:
#             n = int(input(mensagem))
#         except:
#             print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
#         else:
#             return n
#
#
# def input_real(mensagem):
#     while True:
#         try:
#             n = float(input(mensagem))
#         except:
#             print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
#         else:
#             return n

from utilidades_guguebn.dados import input_float, input_int

n_int = input_int('Insira um número inteiro: ')
n_real = input_float('Insira um número real: ')
print(f'Você inseriu o número inteiro {n_int} e o número real {n_real}.')

from time import sleep
from utilidades_guguebn.formatacao import print_center
from utilidades_guguebn.dados import input_int

def opcao(lista):
    print_center('MENU PRINCIPAL')
    for indice, item in enumerate(lista):
        print(f'\033[33m{indice+1}\033[m - \033[36m{item}')
    while True:
        op = input_int('\033[36mSua opção: \033[m')
        if 0 < op <= 3:
            return op
        else:
            print('\033[31mERRO! Digite uma das opções!\033[m')
            sleep(1)


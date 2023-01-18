from time import sleep
from cabecalho import opcao
from utilidades_guguebn.dados import input_int
from arquivo import *  # '*' importa todas as funções

arquivo = 'teste.txt'

if arquivo_existe(arquivo):
    print(f'\033[32mArquivo "{arquivo}" encontrado com sucesso!')
    sleep(1)
else:
    print(f'\033[31mArquivo "{arquivo}" não encontrado!\033[m')
    sleep(1)
    criar_arquivo_txt(arquivo)
    sleep(1)


while True:
    opt = opcao(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opt == 1:
        ler_arquivo(arquivo)
        sleep(3)
    elif opt == 2:
        especial_print('NOVO(S) CADASTRO(S)')
        while True:
            nome = str(input('Nome: ')).strip().title()
            idade = input_int('Idade: ')
            editar_arquivo(arquivo, nome, idade)
            sleep(1.5)
            opc = str(input('\nQuer cadastrar mais alguém [S/N]? ')).strip()[0]
            if opc.upper() == 'N':
                print('Tudo bem')
                sleep(1)
                break
    else:
        sleep(0.7)
        especial_print('Encerrando o sistema... Até logo!')
        sleep(0.7)
        break
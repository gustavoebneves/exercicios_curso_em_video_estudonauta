from time import sleep

def mensagem(msg):
    tamanho_msg = len(msg) + 4
    print(f'\033[1;30;42m{"-" * tamanho_msg:^156}' )
    print(f'\033[1;30;42m  {msg:^152}  ')            # para deixar centralizado no terminal do meu pc
    print(f'\033[1;30;42m{"-" * tamanho_msg:^156}' )
    print('\033[m', end='')


def ajuda(opcao):
    sleep(0.3)
    mensagem(f'Buscando informações sobre "{opcao}"...')
    sleep(1)
    print('\033[7;40m')  # preto e branco
    help(opcao)
    print('\033[m', end='')


while True:
    sleep(2)
    mensagem('SISTEMA DE AJUDA GUGUEBN')
    opc = str(input('Função ou biblioteca (digite "FIM" para encerrar) --> ')).strip()
    if opc.upper() == 'FIM':
        sleep(0.5)
        mensagem('ATÉ A PRÓXIMA')
        sleep(1)
        break
    # não precisa de 'else: '
    ajuda(opc)

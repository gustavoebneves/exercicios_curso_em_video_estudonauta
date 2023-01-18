def escreva(mensagem):
    """
    -> Imprime uma mensagem na tela com contorno de ~
    :param mensagem: mensagem inserida pelo usuário
    :return: nada
    """
    tamanho_msg = len(mensagem) + 4
    print('~'* tamanho_msg)
    print(f'  {mensagem}')
    print('~' * tamanho_msg)

while True:
    msg = str(input('O que você quer imprimir na tela ("nada" para encerrar)? ')).strip().capitalize()
    if msg == 'Nada':
        break
    escreva(msg)
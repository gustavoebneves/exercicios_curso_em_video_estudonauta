def fatorial(numero_input, show=False):
    """
    -> Calcula o fatorial de um número inserido pelo usuário.
    :param numero_input: Número inserido pelo usuário.
    :param show: Opção de mostrar ou não o cálculo.
    :return: Fatorial do número inserido.
    """
    fat = numero_input
    if show:
        print(f'O fatorial de {numero_input} é: {numero_input} x ', end='')
    for numero in range(num-1, 0, -1):
        fat *= numero
        if show:
            if numero > 1 :
                print(numero, end=' x ')
            elif numero == 1:
                print(numero, '=', end=' ')

    if not show:
        print(f'O fatorial de {numero_input} é: ', end='')
    return fat

help(fatorial)
print('__'*31)

print('\nINÍCIO DO PROGRAMA')
print('¨'*18)
num = int(input('Número: '))
opt = str(input(f'Você quer mostrar o calculo do fatorial de {num} [S/N]? ')).strip().lower()[0]
if opt in 's':
    mostrar = True
else:
    mostrar = False
print(fatorial(num, mostrar))




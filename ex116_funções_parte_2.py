        # se nada for passado pro parâmetro, ele recebe 0 !!! PODE SER QUALQUER COISA !!!
def soma_3(a=0, b=0, c=0):
    """
    -> Soma três números inseridos pelo usuário
    :param a:
    :param b:
    :param c:
    :return: no return
    """
    soma = a + b + c
    print(f'{a} + {b} + {c} = {soma:.2f}')


a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))

opt = str(input('Quer mais um valor [S/N]? ')).upper()[0]
if opt not in 'N':
    c = float(input('Terceiro número: '))
    soma_3(a, b, c)
else:
    soma_3(a, b)
    


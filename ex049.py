while True:
    ab = float(input('Insira o comprimento do seguimento AB: '))
    cd = float(input('Insira o comprimento do seguimento CD: '))
    ef = float(input('Insira o comprimento do seguimento EF: '))

    if ab + cd > ef and ab + ef > cd and ef + cd > ab:
        print('\nÉ um triângulo', end=' ')
        if ab == cd == ef:
            print('\033[33mequilátero "todos iguais"\033[m.')
        elif ab != cd != ef != ab:
            print('\033[34mescaleno "todos diferentes"\033[m.')
        else:
            print('\033[35misósceles "dois iguais"\033[m.')
    else:
        print('\033[31mNão é um triángulo\033[m.')
# CORRIGIR
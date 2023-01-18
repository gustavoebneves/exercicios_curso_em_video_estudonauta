def leia_int(msg):
    numero_ou_nao = str(input(msg))
    while True:
        if numero_ou_nao.isnumeric():
            return numero_ou_nao
        else:
            print('\033[0;31mERRO! Insira um número válido\033[m')
            numero_ou_nao = str(input(msg))


n = leia_int('Insira um número: ')
print(f'Você inseriu o número {n}.')

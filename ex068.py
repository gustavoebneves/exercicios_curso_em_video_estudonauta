from time import sleep
opt = -1
while opt != 5:
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira outro número: '))
    opt = int(input('''
    O que você quer fazer com estes números?
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Joga-los fora e inserir novos números;
[5] Sair do programa.
'''))
    while opt != 1 and opt != 2 and opt != 3 and opt != 4 and opt != 5:
        opt = int(input('''
    Opção inválida!
    O que você quer fazer com estes números?
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Joga-los fora e inserir novos números;
[5] Sair do programa.
'''))
    if opt == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')
    elif opt == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
    elif opt == 3:
        print('O maior número entre entre n1 e n2 é: ')
        if n1 > n2:
            print(n1)
        elif n1 < n2:
            print(n2)
        else:
            print('n1 e n2 são iguais.')
    elif opt == 4:
        print('Está bem. Jogando números no lixo', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end=' ')
        sleep(0.5)
        print('Pronto')
        sleep(0.30)
    elif opt == 5:
        print('Está bem.\nAté mais!')
        sleep(2)
    else:
        print('Opção inválida!')

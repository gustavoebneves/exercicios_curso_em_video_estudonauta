from random import randint
ct = 0
while True:
    opt = str(input('Vamos jogar par ou ímpar? '))[0]
    if opt in 'Ss':
        pc = int(randint(1, 10))
        eu = int(input('Você é Par.\nJogue: '))
        s = pc + eu
        if s % 2 == 0:
            print('Você ganhou')
            ct += 1
        else:
            print(f'James Over\nVocê ganhou {ct} vezes.')
            break
    else:
        print(f'Tudo bem. Até mais.\nVocê ganhou {ct} vezes.')
        break

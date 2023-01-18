from random import choice
from time import sleep
esc = int(input('Você quer jogar Pedra, Papel, Tesoura??\n1. Sim.\n2. Não\n'))
lista = ['Pedra', 'Papel', 'Tesoura']
seila = 'sei la'
if esc == 1:
    print('Vamos jogar!!\n')
    while seila != 'Não' and seila != 'Nao':
        sleep(1)
        eu = str(input('\nJogue: ')).strip().lower().capitalize()

        while eu != 'Pedra' and eu != 'Papel' and eu != 'Tesoura':
            print('Ei!! Essa opção não vale!')
            eu = str(input('Jogue: ')).strip().lower().capitalize()
        sleep(0.3)
        print('Pedra...')
        sleep(1)
        print('Papel...')
        sleep(1)
        print('Tesoura...')
        sleep(1)
        pc = choice(lista)
        if (pc == 'Pedra' and eu == 'Tesoura') or (pc == 'Tesoura' and eu == 'Papel') or (pc == 'Papel' and eu == 'Pedra'):
            print('Eu escolhi {} e você {}. \033[31mVocê perdeu\033[m.'.format(pc, eu))
        elif pc == eu:
            print('Eu escolhi {} e você {}. \033[33mNós empatamos\033[m.'.format(pc, eu))
        else:
            print('Eu escolhi {} e você {}. \033[32mVocê ganhou\033[m.'.format(pc, eu))
        sleep(2)
        seila = str(input('Quer continuar??  ')).strip().lower().capitalize()
sleep(1)
print('\nTudo bem. Até mais!')

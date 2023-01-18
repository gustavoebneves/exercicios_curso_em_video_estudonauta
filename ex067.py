from random import randint
from time import sleep
n = randint(1, 10)
tent = 0
n2 = -1
while n2 != n:
    n2 = int(input('Tente adivinhar um número entre 1 e 10: '))
    for i in range(3):
        sleep(0.5)
        print('.')
    sleep(0.5)
    if n2 != n:
        if n2 < n:
            print('Mais... Tenta de novo aí :D\n')
        else:
            print('Menos... Tenta de novo aí :D\n')
    tent += 1

print(f'Você acertou! :D\nParabéns!\nVocê levou {tent} tentativas para acertar.')

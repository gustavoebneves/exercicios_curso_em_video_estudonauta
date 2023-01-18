from random import randint
from time import sleep
n = randint(0, 5)
n2 = int(input('Tente adivinhar um número entre 1 e 5: '))
print('O número que eu pensei foi...')  # , end=''

for i in range(3):
    sleep(1)
    print('Processando...')
sleep(1)
print(n, end='. ')
if n == n2:
    print('Você acertou! :D')
else:
    print('Você errou :C')

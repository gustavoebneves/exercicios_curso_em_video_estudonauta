from time import sleep
from random import randint
print('-=-'*8)
print(f'{"SORTEADOR DA MEGA SENA":^24}')
print('-=-'*8)

jogo_da_vez = []
numero_de_jogos = int(input('Quantos jogo você quer? '))

print('-=-'*8)
print(f'{"SORTEANDO NÚMEROS...":^24}')
print('-=-'*8)

sleep(1.7)
for jogo in range(0, numero_de_jogos):
    # gerador de 6 números aleatórios sem repetição
    for i in range(0, 6):
        numero = randint(1, 60)
        # para não haver repetição de números em uma jogada
        while numero in jogo_da_vez:
            numero = randint(1, 60)
        jogo_da_vez.append(numero)
    jogo_da_vez.sort()
    print(f'{jogo + 1}º jogo: {jogo_da_vez}')
    jogo_da_vez.clear()
    sleep(1)

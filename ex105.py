from random import randint
from operator import itemgetter
from time import sleep
jogadores = {'Gustavo': randint(1, 6),
             'Alisson': randint(1, 6),
             'Bruno': randint(1, 6),
             'Otavio': randint(1, 6)}

for key, value in jogadores.items():
    print(f'{key}: {value}')
    sleep(0.4)

print('\n================= RANKING =================')
                                  # isso pega o índice 1 de jogadores.items() que é o valor tirado no dado
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    sleep(0.4)
    print(f'Em {indice+1}º lugar: O {valor[0]} que tirou {valor[1]} no dado.')

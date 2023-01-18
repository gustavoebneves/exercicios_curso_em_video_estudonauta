todos_jogadores = []
ct = 0
while True:
    ct += 1
    print(f'------------------- {ct}º Jogador -------------------')
    jogador = {'Nome do jogador' : str(input('Nome do jogador: ')).strip().title(),
               'Qtd de partidas jogadas' : int(input('Quantidade de partidas jogadas: ')),
               'Qtd de gols' : 0, 'Gols em cada partida' : []}

    for jogos in range(0, jogador['Qtd de partidas jogadas']):
        gols = int(input(f'Gols na {jogos+1}ª partida: '))
        jogador['Gols em cada partida'].append(gols)
        jogador['Qtd de gols'] += gols
    todos_jogadores.append(jogador.copy())

    opt = str(input('\nQuer adicionar outro jogador [S/N]? ')).strip().upper()[0]
    if opt == 'N':
        break
print(f'\n{"FIM DOS JOGADORES":-^50} \n')

while True:
    opt2 = int(input('Quer ver o aproveitamento de qual jogador (0 encerra)? '))

    while opt2 > len(todos_jogadores) or opt2 < 0:
        print('Opção inválida')
        opt2 = int(input('Quer ver o aproveitamento de qual jogador (0 para encerrar)? '))
    if opt2 == 0:
        break

    print(f'\n{"Aproveitamento do jogador":-^50}')
    print(f'{todos_jogadores[opt2-1]["Nome do jogador"]:-^50} ')
    for indice_key, valor_value in todos_jogadores[opt2-1].items():
        print(f'{indice_key}: {valor_value}.')
    print()

print('\nVolte sempre!')

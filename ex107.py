jogador = {'Nome do jogador' : str(input('Nome do jogador: ')).strip().title(),
           'Qtd de partidas jogadas' : int(input('Quantidade de partidas jogadas: ')),
           'Qtd de gols' : 0, 'Gols em cada partida' : []}

for jogos in range(0, jogador['Qtd de partidas jogadas']):
    gols = int(input(f'Gols na {jogos+1}ª partida: '))
    jogador['Gols em cada partida'].append(gols)
    jogador['Qtd de gols'] += gols

print(f'\n--------- ESTATÍSTICAS DO JOGADOR ---------\n{jogador}')  # solução simples

print('\n--------- ESTATÍSTICAS DO JOGADOR ---------')  # solução bonita
for indice_key, valor_value in jogador.items():
    print(f'{indice_key}: {valor_value}.')

print('\n--------- ESTATÍSTICAS DO JOGADOR ---------')  # solução priorizando os gols
print(f'O jogador {jogador["Nome do jogador"]} jogou {jogador["Qtd de partidas jogadas"]} partidas:')
for partida, goles in enumerate(jogador['Gols em cada partida']):
    print(f'Ele fez {goles} gols na {partida+1}ª partida.')
print(f'Totalizando {jogador["Qtd de gols"]} gols.')

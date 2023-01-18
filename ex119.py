def ficha(nome = '<unknown>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s).')


n = str(input('Nome do jogador: '))
g = str(input('Nº de gols: '))
if g.isnumeric():  # checa se o número de gols pode ser um valor numérico
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
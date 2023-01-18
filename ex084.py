times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',  'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'''5 primeiros colocados: {times[0:5]};
4 últimos colocados: {times[-4:]};
Brasileirão em ordem alfabética: {sorted(times)};
Fortaleza está na {times.index("Fortaleza") + 1}ª posição.''')

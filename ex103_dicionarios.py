filme1 = {
        'titulo' : 'Star Wars',
        'ano' : 1977,
        'diretor' : 'George Lucas'
        }
filme2 = {
        'titulo' : 'Os Vingadores',
        'ano' : 2012,
        'diretor' : 'Joss Whedon'
        }
filme3 = {
        'titulo' : 'Matrix',
        'ano' : 1999,
        'diretor' : 'Irmãos Wachowski'
        }
print(filme1)
print(filme1.values())  # Mostra o valor em cada índice
print(filme1.keys())  # Mostra os nomes dos índices(keys)
print(filme1.items())  # Mostra o valor e o índice
del filme1['diretor']
print(filme1)
filme1['diretor'] = 'George Lucas'
print(filme1)
print('\n')
for key, value in filme1.items():
        print(f'O {key} é {value}.', end=' ')
print('\nLocadora: ')
locadora = [filme1, filme2, filme3]
for key, value in enumerate(locadora):
    print(f'Filme {key+1}: {value}.\n')

print(locadora[0]['titulo'], '\n')

estado = {}
brasil = []
for ct in range(2):
    estado['uf'] = str(input('Insira o estado: '))
    estado['sigla'] = str(input('Insira a sigla do estado: '))
    brasil.append(estado.copy())  # não funciona o [:]. Usar .copy() para DICIONÁRIOS
# para cada estado na lista brasil
for e in brasil:
    # para cada valor em cada estado da lista brasil
    for v in e.values():
        print(v, end=' ')
    print()

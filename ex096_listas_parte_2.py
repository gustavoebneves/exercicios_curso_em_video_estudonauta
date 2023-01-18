pessoas = [['Pedro', 25], ['Maria', 32], ['João', 33]]
print(pessoas)
print(pessoas[0])  # printa inteiro o índice 0 de pessoas
print(pessoas[0][1])  # printa o índice 1 da sublista do índice 0 de pessoas
print(pessoas[0][0][0])  # printa o índice 0 da string/subsublistalista 'Pedro' do índice 0 da sublista da lista pessoas
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera = []
dados = []
for ct in range(0, 3):
    dados.append(str(input('Insira o nome: ')))
    dados.append(int(input('Insira a idade: ')))
    galera.append(dados)
print(galera)  #[['guug', 21, 'aucelora', 45, 'igor', 12], ['guug', 21, 'aucelora', 45, 'igor', 12], ['guug', 21, 'aucelora', 45, 'igor', 12]]

galera = []
dados = []
for ct in range(0, 3):
    dados.append(str(input('Insira o nome: ')))
    dados.append(int(input('Insira a idade: ')))
    galera.append(dados[:])
print(galera)  # [['gugu', 21], ['gugu', 21, 'aucelora', 45], ['gugu', 21, 'aucelora', 45, 'igor', 13]]

galera = []
dados = []
for ct in range(0, 3):
    dados.append(str(input('Insira o nome: ')))
    dados.append(int(input('Insira a idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)  # [['gugu', 21], ['aucelora', 45], ['igor', 12]]



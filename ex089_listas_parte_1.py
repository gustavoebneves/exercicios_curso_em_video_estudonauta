lanches = ['Hambúrger', 'Suco', 'Pizza', 'Pudim']
print(lanches)
lanches.append('Cookie')  # adiciona um novo termo no final da lista
print(lanches)
lanches.insert(0, 'Cachorro-quente')  # usando INSERT, sempre tem que dizer em qual posição se quer adicionar o item
print(lanches)
lanches.pop(0)  # apaga o termo inserido nos parenteses ou o último termo, caso não seja inserido nada
print(lanches)
lanches.pop()
print(lanches)
lanches.insert(0, 'Cachorro-quente')
del lanches[0]    # apaga o termo inserido nos colchetes
print(lanches)
lanches.remove('Pudim')  # apaga o 'valor' inserido. Caso tenha mais de 1 ocorrência, apaga somente a primeira
print(lanches)

valores = list(range(1, 11))  # gera uma lista de 1 até 10
print(valores)
valores = list(range(1, 10, 2))  # gera uma lista de 1 até 10 pulando de 2 em 2
print(valores)
valores = list(range(10, 0, -1))  # gera uma lista de 10 até 1
print(valores)
valores = [8, 2, 3, 5, 6, 4, 10, 9, 1, 7]
print(valores)
valores.sort()  # organiza os valores de forma crescente
print(valores)
valores.sort(reverse=True)  # organiza os valores de forma decrescente
print(valores)
print(len(valores))  # quantidade de termos em valores

valores = list()  # ou valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for numero in valores:
    print(f'Encontrei o valor {numero} na lista!')
print('Fim')
for indice, numero in enumerate(valores):
    print(f'Encontrei o valor {numero} no índice {indice} na lista!')
print('Fim')
del valores
valores = []
for indice in range(1, 4):
    valores.append(int(input('Insira um número: ')))
print(f'Sua lista ficou assim: {valores}.')

a = [2, 3, 4, 7]
b = a  # desse jeito se forma uma ligação entre as duas listas, então se tu alterar o B, também altera o A
b[2] = 8
print(f'\nLista a: {a}')
print(f'Lista b: {b}')
# para que isso não aconteça...
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'\nAgora sem mudar o terceiro termo:\nLista a: {a}')
print(f'Lista b: {b}')

# Exercício de fatiamento têm outras informações sobre listas

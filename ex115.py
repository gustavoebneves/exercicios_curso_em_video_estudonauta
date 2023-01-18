from random import randint
def somapar(lista_num):
    soma_par = 0
    for numero in lista_num:
        if numero % 2 == 0:
            soma_par += numero
    print(f'Sua lista gerada ficou assim: {lista_num};\nA soma de todos os pares da lista foi igual a {soma_par}.')


def sorteia():
    lista = []
    for i in range(0, 5):
        lista.append(randint(1, 100))
    somapar(lista)


sorteia()
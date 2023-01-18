def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


# * empacota os parâmetros e
# os coloca em uma TUPLA
def contador(* seila):
    print(seila)
    print(len(seila))


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def soma_varios(* num):
    soma_seila = 0
    for numero in num:
        soma_seila += numero
    print(soma_seila)

soma(1, 2)
soma(5, 2)
soma(b=1, a=2)
soma(b=5, a=2)

print()
contador(4, 5, 6)
contador(1, 2, 3, 4, 5)
contador(2, 9)

print()
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print()
soma_varios(2, 3, 1, 5, 2, 6, 7)
soma_varios(4, 2, 5, 6, 1)
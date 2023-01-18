lista = []
for ct in range(5):
    num = int(input('Insira um número: '))
    if ct == 0 or num > max(lista):
        lista.append(num)
    elif num < min(lista):
        lista.insert(0, num)
    else:
        for ct2 in range(5):  # varredura de lista !!! IMPORTANTE !!!
            if num <= lista[ct2]:
                lista.insert(ct2, num)
                break
print(lista)

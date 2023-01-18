lista_de_pesos = []
for i in range(5):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(i+1)))
    lista_de_pesos.append(peso)

print('''
Foram entrevistadas {} pessoas
O maior peso desta lista foi: {}Kg
O menor peso desta lista foi: {}Kg\n'''.format(len(lista_de_pesos), max(lista_de_pesos), min(lista_de_pesos)))

# OU

menorp = 0
maiorp = 0
for p in range(5):
    pesos = float(input('Insira o peso da {}ª pessoa: '.format(p+1)))
    if p == 1:
        menorp = pesos
        maiorp = pesos
    else:
        if pesos > maiorp:
            maiorp = pesos

        if pesos < menorp:
            menorp = pesos
print('''
Foram entrevistadas {} pessoas
O maior peso desta lista foi: {}Kg
O menor peso desta lista foi: {}Kg'''.format(p+1, maiorp, menorp))

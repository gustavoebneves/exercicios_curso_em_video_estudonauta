opt = barato = ''
tot = mais_1000 = ct = maisb = 0
while opt not in 'Nn':
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço do produto: '))
    ct += 1
    tot += preco
    if preco > 1000:
        mais_1000 += 1
    if ct == 1 or preco < maisb:
        maisb = preco
        barato = nome
    opt = str(input('\nQuer adicionar mais um produto? ')).strip()
print(f'''
Foram registrados {ct} produtos
Total gasto: R${tot:.2f}
Quantidade de produtos que custam mais de R$1000.00: {mais_1000}
Nome do produto mais barato: {barato}''')

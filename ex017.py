km = float(input('Insira a quantidade de Km rodados: '))
dias = int(input('Insira a quantidade de dias com esse carro: '))

print('Por ter alugado esse carro por {} dias e ter percorrido {}Km, você vai pagar R${:.2f}'.format(dias, km, (dias*60)+(km*0.15)))

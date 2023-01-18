kmh = float(input('Insira sua velocidade: '))

if kmh > 80:
    print('\nMultado! Você passou {}km/h acima do limite de 80km/h.'.format(kmh-80))
    print('O valor da sua multa foi de R${:.2f}.'.format(((kmh-80)*7)+100))

print('\nTenha um bom dia. Dirija com segurança!')

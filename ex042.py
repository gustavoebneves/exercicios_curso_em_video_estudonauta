nome = str(input('Insira seu nome: ')).strip().lower().capitalize()

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome in 'Gabriel Augusto Guilherme':
    print('Esse nome parece o meu!')
elif nome in 'Castiel Uriel Amenadiel Samael':
    print('Você tem nome de anjo!')
else:
    print('Vai tomar no cu, {}!'.format(nome))
    
print('Boa tarde!')

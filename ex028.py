city = input('Insira o nome de uma cidade: ').strip()
city = city.split()
city = city[0].lower()

print('santo' in city)

if 'santo' in city:
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade não começa com Santo')



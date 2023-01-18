ab = float(input('Insira o comprimento do seguimento AB: '))
cd = float(input('Insira o comprimento do seguimento CD: '))
ef = float(input('Insira o comprimento do seguimento EF: '))

if ab + cd > ef and ab + ef > cd and ef + cd > ab:
    print('É um triângulo')
else:
    print('Não é um triángulo.')

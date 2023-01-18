from math import sqrt, pow
op, ad = input('Insira o cateto oposto e o cateto adjascente respectivamente: ').split(' ')
op = float(op)
ad = float(ad)

print('A hipotenusa deste triângulo retângulo é: {:.3f}'.format(sqrt(pow(op, 2)+pow(ad, 2))))
                                                                # ou: hi = sqrt(pow(op, 2)+pow(ad, 2))

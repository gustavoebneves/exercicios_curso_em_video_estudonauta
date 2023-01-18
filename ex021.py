from math import cos, tan, sin, radians
ang = input('Insira um ângulo em graus: ')
ang = float(ang)
ang2 = radians(ang)
print('O cosseno do ângulo {:.2f}º é: {:.4f}\nSeu seno é: {:.4f}\nSua tangente é: {:.4f}'.format(ang, cos(ang2), sin(ang2), tan(ang2)))

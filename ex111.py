def area(c, l):
    """
    -> Calcula a área de um terreno retangular.
    :param c: comprimento/length
    :param l: largura/width
    :return: sem retorno/no return
    """
    a = c * l
    print(f'A área do seu terreno {c}m x {l}m é de {a:.2f}m²')


comprimento = float(input('Insira o comprimento do seu terreno: '))
largura = float(input('Insira a largura do seu terreno: '))
area(comprimento, largura)

help(area)
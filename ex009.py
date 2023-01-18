n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
media = (n1+n2)/2

print('A média do aluno é: {}'.format(media), end=' ')
if media >= 6:
    print('Aprovado! :D')
else:
    print('Reprovado :(')

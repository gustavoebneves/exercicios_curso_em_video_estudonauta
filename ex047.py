n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

if (n1+n2)/2 >= 7:
    print('APROVADO :D')
elif (n1+n2)/2 < 5:
    print('REPROVADO :C')
elif 5 <= (n1 + n2)/2 <= 6.9:
    print('EXAME\nEstude mais!')

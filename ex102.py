print('-=-=-'*11)
planilha = []
aluno = []

while True:
    nome = str(input('Insira o nome do aluno (digite "parar" para interromper): ')).strip().lower().title()
    if nome == 'Parar':
        break
    aluno.append(nome)
    aluno.append(float(input(f'Insira a primeira nota de {nome}: ')))
    aluno.append(float(input(f'Insira a segunda nota de {nome}: ')))
    planilha.append(aluno[:])
    aluno.clear()
    print('-=-=-' * 11)

print('\n<=>'*20)
situacao = ''
for n_aluno, alun in enumerate(planilha):
    nome = planilha[n_aluno][0]
    media = (planilha[n_aluno][1] + planilha[n_aluno][2]) / 2
    if media >= 7:
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'
    print(f'{n_aluno+1}º aluno(a): {nome}.  Média: {media}.  Situação: {situacao};')

opc = str(input('\nVocê quer ver as notas de algum ou aguns alunos? [S/N] ')).strip().upper()[0]
if opc in 'S':
    while True:
        opc2 = int(input('\nQual aluno (Digite "0" para encerrar o programa)? ' ))
        if opc2 == 0:
            print('\nVOLTE SEMPRE')
            break
        else:
            print(planilha[opc2-1])
else:
    print('\nVOLTE SEMPRE')

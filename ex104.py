aluno = {'nome' : str(input('Insira o nome do aluno: ')), 'media' : float(input('Insira a média do aluno: '))}
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif 5 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
print('-=-'*15)
for key, value in aluno.items():
    print(f'-{key} é igual a {value}')

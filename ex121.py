def notas():
    """
    -> Sistema de cálculo de média de turma e aproveitamento.
    :return: Planilha (lista) contendo todos os dados referente às notas e ao aproveitamento
    """
    planilha_aluno = dict()
    planilha_geral = list()
    ct = mgeral = ctn = maior = 0
    menor = 11
    while True:
        ct += 1
        nt = 0
        planilha_aluno['Nome'] = str(input(f'Nome do {ct}º aluno: ')).strip().title()

        nt += 1
        planilha_aluno['Nota 1'] = float(input(f'{nt}ª nota do aluno: '))
        ctn += 1

        # maior e menor nota 1
        if planilha_aluno['Nota 1'] > maior:
            maior = planilha_aluno['Nota 1']
        if planilha_aluno['Nota 1'] < menor:
            menor = planilha_aluno['Nota 1']

        nt += 1
        planilha_aluno['Nota 2'] = float(input(f'{nt}ª nota do aluno: '))
        ctn += 1

        # maior e menor nota 2
        if planilha_aluno['Nota 2'] > maior:
            maior = planilha_aluno['Nota 2']
        if planilha_aluno['Nota 2'] < menor:
            menor = planilha_aluno['Nota 2']

        # media aluno
        planilha_aluno['Media'] = (planilha_aluno['Nota 1'] + planilha_aluno['Nota 2'])/2

        # Média geral
        mgeral += planilha_aluno['Media']

        # Situação do aluno
        if planilha_aluno['Media'] >= 7:
            planilha_aluno['Situação'] = 'Aprovado'
        elif 7 > planilha_aluno['Media'] >= 5:
            planilha_aluno['Situação'] = 'Recuperação'
        else:
            planilha_aluno['Situação'] = 'Reprovado'

        # colocar o dicionário do aluno dentro da lista geral
        planilha_geral.append(planilha_aluno.copy())

        opt = str(input('\nQuer adicionar mais um aluno [S/N]? ')).strip().lower()[0]
        if opt == 'n':
            planilha_geral.append(maior)
            planilha_geral.append(menor)
            planilha_geral.append(ctn)
            planilha_geral.append(mgeral/ct)
            return planilha_geral


help(notas)
print('__'*80)
print('\nINÍCIO DO PROGRAMA')
print('¨'*18)

planilha = notas()
ct = ct2 = 1
print('\n----------------- PLANILHA GERAL -----------------\n')
for i in range(len(planilha)):
    if type(planilha[i]) is dict:
        print(f'  {ct2}º aluno')
        for key, value in planilha[i].items():
            print(f'{key}: {value}.')
        print()
        ct2 += 1
    else:
        if ct == 1:
            print(f'Maior nota: {planilha[i]};')
        elif ct == 2:
            print(f'Menor nota: {planilha[i]};')
        elif ct == 3:
            print(f'Número de notas: {planilha[i]};')
        elif ct == 4:
            print(f'Média da turma: {planilha[i]:.2f}.')
        ct += 1

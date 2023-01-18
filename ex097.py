pessoas = []
dados = []
maisp = []  # mais de 100
maisl = []  # menos de 70
qt = opt = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if pessoas[qt][1] >= 100:
        maisp.append(pessoas[qt])
    elif pessoas[qt][1] <= 70:
        maisl.append(pessoas[qt])

    opt = str(input('Quer continuar? [S/N]: '))[0]
    dados.clear()

    if opt in 'nN':
        break
    qt += 1

print(f'''\nVocê cadastrou {qt+1} pessoas.\n{len(maisp)} delas estão acima dos 100Kg, que são: {maisp}.
{len(maisl)} delas estão abaixo dos 70Kg, que são: {maisl}.''')

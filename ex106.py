from datetime import date

ano_atual = int(date.today().year)
cadastro = {'nome' : str(input('Nome: ')).strip().title(),
            'ano de nascimento' : int(input('Ano de nascimento: ')),
            'carteira de trabalho' : int(input('Carteira de trabalho (0 se não tiver): '))}
cadastro['idade'] = ano_atual - cadastro['ano de nascimento']

if cadastro['carteira de trabalho'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ano de contratação'] + 35) - ano_atual)

print('\n------- SEUS DADOS -------\n')
for indice, valor in cadastro.items():
    if indice == 'carteira de trabalho' and cadastro['carteira de trabalho'] == 0:
        print(f'{indice}: Não tem.')
    elif indice == 'salário':
        print(f'{indice}: R$ {valor}.')
    else:
        print(f'{indice }: {valor}.')

from datetime import date

ano = int(input('Insira um ano para saber se é bissexto. Insira "0" para analizar o ano atual:  '))
if ano == 0:
    ano = date.today().year
    print('O seu ano ano atual de {}'.format(ano), end=' ')
else:
    print('O ano de {}'.format(ano), end=' ')

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('é bissexto.')
else:
    print('não é bissexto.')

import datetime as dt
ano = int(input('Insira o ano que você nasceu: '))
anoat = dt.date.today().year
idade = anoat - ano

if idade < 18:
    print('Ainda não é hora de você se alistar. Falta(am) {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Está na hora de você se alistar!')
elif idade > 18:
    print('Já passou da idade de você se alistar. Já passou(aram) {} ano(os).'.format(idade - 18))

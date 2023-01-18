print('Boa tarde!')
casa = float(input('Qual o valor da casa que você deseja comprar? R$ '))
sal = float(input('Qual seu salário? R$ '))
meses = int(input('Em quantos meses você vai querer parcelar? '))

prest = casa/meses
print('A mensalidade ficará em R$ {:.2f}'.format(prest))

if prest >= 0.30 * sal:
    print('\nInfelizmente seu impréstimo foi negado.')
else:
    print('Seu impréstimo foi aprovado.')
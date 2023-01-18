from datetime import date
anoat = date.today().year
maior = 0
menor = 0
for i in range(7):
    ano = int(input('Insira o ano de nascimento: '))
    idade = anoat - ano
    if idade > 18:
        maior = maior + 1
    elif idade < 18:
        menor = menor + 1
print('{} das 7 pessoas esta(ão) na maioridade e {} esta(ão) na menoridade.'.format(maior, menor))

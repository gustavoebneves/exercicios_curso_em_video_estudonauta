media_idade = 0
maior_idade = 0
nome_mais_velho = 'SEILA'
menor_20 = 0

for i in range(4):
    print('{:=^30}'.format(' {}ª PESSOA ').format(i+1))
    nome = str(input('Insira o nome: ')).strip().lower().title()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo: ')).strip().lower().capitalize()

    # média das idades
    media_idade += idade

    # homem mais velho
    if i == 1:
        maior_idade = idade
    elif i > 0 and sexo == 'Masculino':
        if idade >= maior_idade:
            maior_idade = idade
            nome_mais_velho = nome

    # quantidade de mulheres com menos de 20 anos
    if sexo == 'Feminino' and idade < 20:
        menor_20 += 1

media_idade = media_idade / (i+1)
print('''Foram entrevistadas {} pessoas;
Média de idade dos entrevistados: {};
Nome do homem mais velho: {};
Quantidade de mulheres com menos de 20 anos: {}.'''.format(i+1, media_idade, nome_mais_velho, menor_20))

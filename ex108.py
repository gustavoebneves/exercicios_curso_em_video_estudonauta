planilha = []
pessoa = {}
media_idade = 0
mulheres = []
acima_media = []
while True:
    nome = str(input('\nNome: ')).strip().title()
    if nome == 'Parar' :
        break
    sexo = str(input('Sexo: ')).strip().title()[0]
    while sexo not in 'FM':
        sexo = str(input('Opção inválida\nSexo: ')).strip().title()[0]
    idade = int(input('Idade: '))
    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = idade
    # media de idades
    media_idade += idade
    # lista de mulheres
    if sexo == 'F':
        mulheres.append(nome)

    planilha.append(pessoa.copy())

# lista de pessoas com idade acima da média
for indice, valor in enumerate(planilha):
    if planilha[indice]['Idade'] > media_idade/len(planilha):
        acima_media.append(planilha[indice].copy())

print(f'''\n------------------ RESULTADO DA PESQUISA ------------------
\n{len(planilha)} pessoas foram cadastradas;
A média de idade foi de {media_idade/len(planilha):.2f} anos;
As seguintes mulheres foram cadastradas: {mulheres};
As seguintes pessoas estão com a idade acima da média: {acima_media}.''')

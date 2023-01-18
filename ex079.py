opt = 's'
hom = mul_20 = maiores = ct = 0
while opt != 'n':
    idade = int(input('\nInsira a idade da pessoa: '))
    sexo = str(input('Insira o sexo da pessoa: '))
    while sexo not in 'FfMm':
        print('Opção inválida')
        sexo = str(input('Insira o sexo da pessoa: '))
    ct += 1
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        hom += 1
    if sexo in 'Ff' and idade < 20:
        mul_20 += 1
    opt = str(input('Quer continuar? '))
    while opt not in 'SsNn':
        print('Opção inválida')
        opt = str(input('Quer continuar? '))
print(f'''
* Foram entrevistadas {ct} pessoas;
* {maiores} delas são maiores de idade;
* {hom} são homens;
* {mul_20} são mulheres com menos de 20 anos.''')

sexo = str(input('Insira o seu sexo: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Opção inválida\nInsira o seu sexo: ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso.')

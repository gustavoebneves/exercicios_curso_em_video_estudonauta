while True:
    peso = float(input('Insira seu peso em Kg: '))
    altura = float(input('Insira sua altura em m: '))
    imc = peso / (pow(altura, 2))
    print('Seu IMC é de {:.2f}Kg/m². Você está '.format(imc), end='')
    if imc < 18.5:
        print('\033[36mabaixo do peso\033[m.')
    elif 25 > imc >= 18.5:
        print('no \033[32mpeso ideal\033[m.')
    elif 30 > imc >= 25:
        print('em \033[36msobrepeso\033[m.')
    elif 40 > imc >= 30:
        print('com \033[33mobesidade\033[m.')
    elif imc > 40:
        print('com \033[31mobesidade mórbida\033[m.')

s = float(input('Insira seu salário: R$'))

if s > 1250:
    print('O aumento do seu salário foi de: R${:.2f}\nSalário final: \033[32m{}'.format(0.10 * s, 0.10 * s + s))
else:
    print('O aumento do seu salário foi de: R${:.2f}\nSalário final: \033[32m{}'.format(0.15 * s, 0.15 * s + s))

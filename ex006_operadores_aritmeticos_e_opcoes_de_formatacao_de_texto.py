n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
potenciacao = n1**n2
radiciacao = n1**(1/n2)
divisao_inteira = n1//n2
resto_da_divisao = n1%n2

print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
print('A subtração entre {} e {} é: {}'.format(n1, n2, subtracao))
print('A multiplicação entre {} e {} é: {}'.format(n1, n2, multiplicacao))
print('A divisão entre {} e {} é: {}'.format(n1, n2, divisao))
print('{} elevado a {} é: {}'.format(n1, n2, potenciacao))
print('A raiz {} de {} é: {:.3f}'.format(n2, n1, radiciacao))
                         #^^^^^^ serve para deixar o número com 3 casas depois da vírgula
print('A divisão inteira entre {} e {} é: {}'.format(n1, n2, divisao_inteira))
print('O resto da divisão entre {} e {} é: {}'.format(n1, n2, resto_da_divisao))
print('Olá,', end=' ')
            #^^^^^^^^ faz não ocorrer quebra de linha entre "prints"
print('mundo!')
print('Olá,\nmundo!')
          #^^ quebra linhas

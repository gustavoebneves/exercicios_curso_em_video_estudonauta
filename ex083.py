numeros = ('Zero', 'Um', 'Dois', 'Três',  'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
n = int(input('Insira um número entre 0 e 10: '))
while n < 0 or n > 10:
    n = int(input('Tente novamente. Insira um número entre 0 e 10: '))
print(f'Você digitou o número: {numeros[n]}.')

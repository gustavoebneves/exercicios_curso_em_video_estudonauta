opt = 1
ct = maior = menor = media = 0
while opt != 2:
    n = int(input('Insira um número: '))
    ct += 1
    media += n
    if ct == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opt = int(input('Você quer continuar?\n[1] Sim\n[2] Não\n'))
print(f'O maior número digitado foi {maior} e o menor foi {menor}\nA média dos números digitados foi {media/ct}')

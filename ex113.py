from time import sleep
def contaduro(inicio, final, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < final:
        ct = inicio
        while ct <= final:
            sleep(0.17)
            print(ct, end=' ')
            ct += passo
    elif inicio > final:
        ct = inicio
        while ct >= final:
            sleep(0.17)
            print(ct, end=' ')
            ct -= passo
    print('FIM')


contaduro(1, 10, 1)
contaduro(10, 0, 2)
print('-- Faça sua contagem --')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contaduro(ini, fim, pas)

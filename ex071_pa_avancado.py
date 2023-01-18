print('-=-'*8)
print('{:^24}'.format('Gerador de PA avançado'))
print('-=-'*8)

n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
nt = 0

opt = 1
while opt != 0:
    if nt == 0:
        opt = int(input('\nVocê quer quantos termos da PA? '))
    else:
        opt = int(input('\nVocê quer quantos termos a mais? '))
    nt = 0
    while nt != opt:
        nt += 1
        print(n1, end=' -> ')
        n1 += r
    print('Pausa')
print('\nEstá bem. Até mais!')

print('-=-'*8)
print('{:^24}'.format('Gerador Fibonacci'))
print('-=-'*8)
ft = int(input('Quantos termos de Fibonacci você quer: '))
f1 = 0
f2 = int(1)

print('{} -> {}'.format(f1, f2), end=' -> ')
ct = 0

while ct < (ft - 2):
    f3 = f1 + f2
    print('{}'.format(f3), end=' -> ')
    ct += 1
    f1 = f2
    f2 = f3

print('Fim')

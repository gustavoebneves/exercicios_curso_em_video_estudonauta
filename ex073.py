n = s = ct = 0
while n != 999:
    n = int(input('Insira um número: '))
    if n != 999:
        s += n
        ct += 1
print(f'Foram digitados {ct} números e a soma deles é: {s}')

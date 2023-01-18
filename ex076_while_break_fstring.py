n = ct = s = 0
nome = str(input('Insira seu nome: ')).capitalize()
while True:
    n = int(input('Insira um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    ct += 1
# exemplo fstring
print(f'Olá {nome:=^20}.\nForam inseridos {ct} números e a soma deles foi igual a {s:.2f}')

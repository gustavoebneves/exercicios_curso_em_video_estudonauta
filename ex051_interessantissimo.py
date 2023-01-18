from time import sleep
import pyttsx3
text_speech = pyttsx3.init()

# Saudações
print('-=-'*8)
print('{:^24}'.format('MINIMERCADO JA'))
print('-=-'*8)
ola = 'MINIMERCADO JA'
text_speech.say(ola)
text_speech.runAndWait()
ola = 'Olá!'
text_speech.say(ola)
text_speech.runAndWait()

# Escolha adicionar/pagar
preco_add = preco2 = preco_final = 0
op = int(input('Opções: \n[1] Adicionar produto.\n[2] Forma de pagamento.\n'))
while op != 1 and op != 2:
    print('\033[31mOpção inválida\033[m.')
    op = int(input('Opções: \n[1] Adicionar produto.\n[2] Forma de pagamento.\n'))

while op == 1:
    preco_add = float(input('Insira o preço do produto R$ '))
    preco2 = preco2 + preco_add
    op = int(input('Opções: \n[1] Adicionar produto.\n[2] Forma de pagamento.\n'))

# Forma de pagamento
sleep(1)
print(f'''Valor total da compra: R$ {preco2:.2f}
Formas de pagamento: (número à esquerda da opção)
[1] À vista dinheiro/cheque: 10% de desconto;
[2] À vista cartão: 5% de desconto;
[3] 2x no cartão: Sem juros/desconto;
[4] 3x ou mais no cartão: 20% de juros.''')

forpag = int(input('Forma de pagamento: '))
sleep(1)
while forpag != 1 and forpag != 2 and forpag != 3 and forpag != 4:
    print('\n\033[31mForma de pagamento inválida\033[m.')
    forpag = int(input('Forma de pagamento: '))
sleep(0.4)
if forpag == 1:
    print('\nForma de pagamento escolhida: À vista dinheiro/cheque: 10% de desconto.')
    preco_final = preco2 - (preco2 * 0.1)
    print(f'Preço final: R$ {preco_final:.2f}')
elif forpag == 2:
    print('\nForma de pagamento escolhida: À vista cartão: 5% de desconto.')
    preco_final = preco2 - (preco2 * 0.05)
    print(f'Preço final: R$ {preco_final:.2f}')
elif forpag == 3:
    print('\nForma de pagamento escolhida: 2x no cartão: Sem juros/desconto.')
    print(f'Preço final: R$ {preco2:.2f} | 2x de R$ {preco2 / 2:.2f}')
elif forpag == 4:
    parc = int(input('Quantidade de parcelas: '))
    sleep(0.6)
    print('\nForma de pagamento escolhida: 3x ou mais no cartão: 20% de juros.')
    preco_final = preco2 + (preco2 * 0.20)
    sleep(0.6)
    print(f'Preço final: R$ {preco_final:.2f} | {parc}x de R$ {preco_final / parc:.2f} com 20% de juros.')

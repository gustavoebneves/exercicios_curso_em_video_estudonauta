km = int(input('Insira os km da viagem: '))

if km <= 200:
    print('Você vai pagar R${:.2f}'.format(km*0.5))
else:
    print('Você vai pagar R${:.2f}'.format(km*0.45))


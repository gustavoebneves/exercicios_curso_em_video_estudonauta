expressao = str(input('Insira sua expressão matemática: '))
parenteses = []
# cria uma lista de controle de processo
# a cada '(' coloca um '(' numa lista separada
# a cada ')' remove um '(' da lista 
# no final faz a contagem
for caractere in expressao:
    if caractere == '(':
        parenteses.append('(')
    elif caractere == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')

if len(parenteses) > 0:
    print('Sua expressão está errada. Lembre-se de fechar os parenteses.')
elif len(parenteses) == 0:
    print('Sua expressão está correta!')

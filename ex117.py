def voto(nasc):
    from datetime import datetime
    idade = datetime.today().year - nasc
    idade_situ = [idade]
    if idade < 16:
        idade_situ.append('NEGADO')
    elif 18 > idade >= 16 or idade > 65:
        idade_situ.append('OPCIONAL')
    else:
        idade_situ.append('OBRIGATÓRIO')
    return idade_situ


ano = int(input('Insira seu ano de nascimento: '))
idade_situacao = voto(ano)
print(f'Sua idade é de {idade_situacao[0]} anos e sua situação eleitoral é de voto {idade_situacao[1]}.')

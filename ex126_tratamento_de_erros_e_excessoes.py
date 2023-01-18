try:  # tentativa de algo
    num = int(input('Numerador: '))
    den = int(input('Denominador: '))
    res = num/den
except (ValueError, TypeError):  # deu erro/mostrar erro/fazer alguma coisa por causa de determinado erro com a tentativa
    print('Infelizmente tivemos um problema com o tipo de dado que você informou :(')
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')
except KeyboardInterrupt:
    print('O usuário preferiu encerrar o programa')
except Exception as erro:
    print(f'Infelizmente ocorreu o erro {erro.__class__} no seu programa')
else:  # se não deu erro faz isso
    print(f'O resultado é igual a: {res:.2f}')
finally:  # vai acontecer sempre com erro ou não
    print('Volte sempre consagrado')

# lista de erros e excessões em python https://docs.python.org/pt-br/3/tutorial/errors.html (ctrl+botão esquerdo)
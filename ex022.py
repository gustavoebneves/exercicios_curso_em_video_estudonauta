from random import choice
n1, n2, n3, n4 = input('Insira o nome dos alunos: ').split(' ')
alunos = [n1, n2, n3, n4]
print('O aluno escolhido para apagar o quadro foi: {}'. format(choice(alunos)))

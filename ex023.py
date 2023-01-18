from random import shuffle
n1, n2, n3, n4 = input('Insira o nome dos alunos: ').split(' ')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem, de alunos para apresentação foi: {}'.format(alunos))

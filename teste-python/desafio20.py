import random

alunos = []

c = 0
while (c < 4):
    aluno = input('Digite o nome do {}º aluno: '.format(c + 1))
    alunos.append(aluno)
    c = c + 1

random.shuffle(alunos)

c2 = 0
while (c2 < 4):
    print('{}º aluno {}'.format((c2 + 1), alunos[c2]))
    c2 = c2 + 1

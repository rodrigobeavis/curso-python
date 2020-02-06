import random

alunos = []

c = 0
while(c < 4):
 aluno = input('Digite o nome do {}º aluno: '.format(c+1))
 alunos.append(aluno)
 c = c + 1


sorteio = random.randint(0, 8)
print(sorteio)
print('O aluno sorteado foi {}'.format(alunos[sorteio]))
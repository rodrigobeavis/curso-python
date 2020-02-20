import random


print('Jokenpô')

print('1 - tesoura \n 2 - pedra \n 3 - papel')

userSelect = int(input('Escolha uma opção: '))

pcSelect = random.randint(1, 3)

text = ['tesoura', 'pedra', 'papel']

print('Você {} Vs Máquina {}'.format(text[userSelect - 1], text[pcSelect - 1]))
if (pcSelect == 1 and userSelect == 2) or (pcSelect == 2 and userSelect == 1) or (pcSelect == 3 and userSelect == 2):
    print('A máquina você perdeu.')
elif (userSelect == 1 and pcSelect == 2) or (userSelect == 2 and userSelect == 1) or (userSelect == 3 and pcSelect == 2):
    print('A máquina você ganhou.')
else:
    print('Empate')
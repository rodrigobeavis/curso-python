import random

numRandom = random.randint(0, 5)

numUser = int(input('Tente Adivinhar um número de 0 a 5 que o computador escolheu: '))

if numRandom == numUser:
    print('# # Acertou # #')
else:
    print('!!! Errou !!!')
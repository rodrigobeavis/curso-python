numeros = []

print('Digite 3 números e descubra qual é o maior.')

cont = 0
while cont < 3:
    numeros.append(int(input('Digite o {}º número '.format(cont+1))))
    cont += 1
numeros.sort()

print('O maio número é {} e o menor é {}'.format(numeros[2], numeros[0]))
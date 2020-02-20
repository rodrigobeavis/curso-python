compRetas = []

print('Digite 3 números e descubra qual é o maior.')

cont = 0
while cont < 3:
    compRetas.append(int(input('Digite o comprimento da reta {} '.format(cont + 1))))
    cont += 1

if (compRetas[0] + compRetas[1] > compRetas[2] > compRetas[0] - compRetas[1]) | (
        compRetas[0] + compRetas[2] > compRetas[1] > compRetas[0] - compRetas[2]) | (
        compRetas[1] + compRetas[2] > compRetas[0] > compRetas[1] - compRetas[2]):
    print('As três retas formam um triângulo ')

    if compRetas[0] == compRetas[1] == compRetas[2] and compRetas[0] == compRetas[2] == compRetas[1] and compRetas[1] == compRetas[0] == compRetas[2]:
        print('do tipo Equilátero')
    elif compRetas[0] == compRetas[1] or compRetas[0] == compRetas[2] or compRetas[1] == compRetas[2]:
        print('do tipo Isósceles')
    else :
        print('do tipo Escaleno')


else:
    print('As três retas NÃO formam um triângulo.')

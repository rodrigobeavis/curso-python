

pesos = []

for count in range(0, 5):
    pesos.append(int(input('Digite o peso da {}º pessoa: '.format(count+1))))

pesos.sort()

print('A pessoa com maior possuí {} a pessoa com menor possuí {}'.format(pesos[0], pesos[4]))
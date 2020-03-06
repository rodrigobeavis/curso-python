print('PA')
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

textPA = ''
lastNumber = primeiroTermo
for c in range(1, 10):
    lastNumber += razao
    textPA += '{}, '.format(lastNumber)

print('A os 10 primeiros números da PA são: ({}) '.format(textPA[:-2]))
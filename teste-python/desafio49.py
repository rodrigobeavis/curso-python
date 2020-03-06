
num = int(input('Digite um número para ver a tabuada do mesmo: '))

for c in range(1, 10, 1):
    print('{} X {} = {}'.format(num, c, int(num * c)))
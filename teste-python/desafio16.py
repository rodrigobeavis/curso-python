import math

num = float(input('Digite um número real: ').replace(',', '.'))

print('A parte inteira do número é {}.'.format(math.trunc(num)))
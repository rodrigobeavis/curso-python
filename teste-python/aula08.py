from math import sqrt, floor, ceil

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f} .'.format(num, raiz))


print('A raiz de {} é igual a {:.3f} .'.format(num, floor(raiz)))


print('A raiz de {} é igual a {:.2f} .'.format(num, ceil(raiz)))
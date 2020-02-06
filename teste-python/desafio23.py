numero = input('Digite um número de 0 a 9999: \n').strip()

numeroInt = int(numero)


print('Unidade {}'.format(numeroInt % 10))
print('Dezena {}'.format((numeroInt % 100) // 10))
print('Centena {}'.format((numeroInt % 1000) // 100))
print('Milhar{}'.format((numeroInt % 10000) // 1000))


"""

print('Unidade {}'.format(numero[-1]))
print('Dezena {}'.format(numero[-2]))
print('Centena {}'.format(numero[-3]))
print('Milhar {}'.format(numero[-4]))

"""
num = int(input('Digite um número: '))

print('Taboada para número {}'.format(num))
contador = 1
while contador < 10:

    resultado = contador * num
    print('{} X {} = {}'.format(contador, num, resultado))
    contador += 1


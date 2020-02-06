from math import tan, sin, cos



angulo = float(input('Digite um ângulo para calcular seno, cosseno e tangente: ').replace(',', '.'))


seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)


print('Seno {0:.2f}'.format(seno))
print('Cosseno {0:.2f}'.format(cosseno))
print('Tangente {0:.2f}'.format(tangente))
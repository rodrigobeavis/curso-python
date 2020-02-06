from math import pow, sqrt

print('Calcular o cateto oposto de um triângulo retangulo')

catetoOposto = float(input('Digite o Cateto oposto: ').replace(',', '.'))
catetoAdjacente = float(input('Digite o Cateto adjacente: ').replace(',', '.'))


hipotenusa = pow(catetoAdjacente,2) +pow(catetoOposto,2)

hipotenusa = sqrt(hipotenusa)

print('A hipotenusa do triãngulo retângulo é {0:.2f}'.format(round(hipotenusa, 2)))

altura = float(input('Digite a altura: ').replace(',', '.'))
largura = float(input('Digite a largura: ').replace(',', '.'))

areaTotal = altura * largura

print('Serão necessários {0:.2f} litros de tinta.'.format(round((areaTotal / 2), 2)))

reais = float(input('Digite o valor em Reais (BRL) com ponto: ').replace(',', '.'))


print('A cotação atual é US$ 1,00 = R$ 3,27, então você pode comprar US$ {0:.2f}'.format(round(reais/3.27)) )
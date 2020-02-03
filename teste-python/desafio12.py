preco = float(input('Digite o preço atual: ').replace(',', '.'))

preco -= (preco * 0.05)
preco = round(preco, 2)
print('O valor com  desconto de 5% é {0:.2f}'.format(preco))
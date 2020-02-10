salario = float(input('Digite um salário para alicar o reajueste conforme faixa: ').replace(',', '.'))

if salario >= 1250.00:
    salario += (salario * 0.10)
else:
    salario += (salario * 0.15)

print('O salário atual será de {:.2f}'.format(round(salario, 2)))
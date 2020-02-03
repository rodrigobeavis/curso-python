salario = float(input('Digite o salário do funcionário (R$ 0,00): ').replace('.', '').replace(',', '.'))

salario += salario * 0.15

print('O salário do funcionário mais 15% é R${0:.2f}'.format(salario))
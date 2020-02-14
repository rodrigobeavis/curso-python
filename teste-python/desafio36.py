valorCasa = float(input("Digite o valor da casa: ").replace(',', '.'))
salario = float(input("Digite o valor do salário: ").replace(',', '.'))
tempoEmAnos = float(input("Digite o número de anos: ").replace(',', '.'))


valorPestacao = valorCasa / (tempoEmAnos * 12)


if valorPestacao < (salario * 0.3):
    print('Aprovado')
else:
    print('Reprovado')




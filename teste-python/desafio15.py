km = float(input('Digite a quantidade de KM: ').replace(',', '.'))
dias = int(input('Digite o número de dias: '))

valorfinal = (dias * 60) + (km * 0.15)

print('\n\nO valor a pagar será R${:.2f}'.format(round(valorfinal, 2)))
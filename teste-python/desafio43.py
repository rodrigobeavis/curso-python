altura = float(input('Digite sua altura: ').replace(',', '.'))
peso = float(input('Digite seu peso: ').replace(',', '.'))

imc = peso / (pow(altura, 2))

print('IMC = {}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Você está com peso ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')



velocidade = int(input('Digite a velocidade do veículo: '))

if velocidade > 80:
    valor = (velocidade - 80) * 7.00
    print('O veículo foi multado em R$ {:.2f}'.format(valor))
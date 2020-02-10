
distancia = int(input('Digite um a distância da viagem: '))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print('O valor da viagem é R$ {:.2f}'.format(valor))
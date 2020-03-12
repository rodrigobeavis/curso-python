import datetime
import math

QuantMaioresDeIdade = 0

for count in range(0, 7):
    dataNascimento = input("Digite a data de nascimento: ")

    dias, mes, ano = map(int, dataNascimento.split('/'))
    dataNascimento = datetime.date(ano, mes, dias)
    dataAtual = datetime.date.today()
    idade = math.trunc((dataAtual - dataNascimento).days / 365)
    if idade >= 18 :
        QuantMaioresDeIdade += 1

print('Quantidade de pessoas maiores de idade: {}'.format(QuantMaioresDeIdade))
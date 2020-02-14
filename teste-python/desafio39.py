import datetime
import math

dataNascimento = input("Digite a data de nascimento: ")

dias, mes, ano = map(int, dataNascimento.split('/'))
dataNascimento = datetime.date(ano, mes, dias)
dataAtual = datetime.date.today()

idade = math.trunc((dataAtual - dataNascimento).days / 365)

print('Você possuí {} anos'.format(idade))

if idade in [18, 17]:
    print('Você deve se alistar.')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(idade - 18))
elif idade < 17:
    print('Faltam {} anos para o alistamento'.format(17 - idade))

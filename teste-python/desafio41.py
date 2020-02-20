import datetime

anoNascimento = int(input('Digite o anos de nascimento do atleta: '))

idadeAtual = datetime.date.today().year - anoNascimento

if idadeAtual <= 9:
    print('Mirim')
elif idadeAtual <= 14:
    print('Infantil')
elif idadeAtual <= 19:
    print('Junior')
elif idadeAtual <= 20:
    print('Sênior')
elif idadeAtual > 20:
    print('Master')

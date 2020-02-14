
import cores

dia = input('{}Qual o dia do seu nascimento ?{}'.format(cores.get('am'), cores.get('l')))
mes = input('{}Qual é o mês que você nasceu ?{}'.format(cores.get('am'), cores.get('l')))
ano = input('{}Qual é o ano que você nasceu ?{}'.format(cores.get('am'), cores.get('l')))

print('Dia: ', dia)
print('Mês: ', mes)
print('Ano: ', ano)

print('você nasceu no dia ', dia , 'do mês ', mes, ' no ano ', ano, ', correto?')

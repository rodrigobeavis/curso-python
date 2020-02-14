nome = input('Qual é seu nome? \n')

if nome.lower() == 'gustavo':
    print('----OK----')
elif nome.lower() == 'pedro' | nome.lower() == 'maria' | nome.lower() == 'paulo' :
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome Feminino')
else:
    print('==== False ====')

print('Tenha um bom dia, {} !'.format(nome))
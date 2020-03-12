
listaDePessoas = []
pessoa = object

for c in range(0,5):

    print('Digite os dados da pessoa {}º \n'.format(c+1))
    """nome = input('nome: ')
            sexo = input('sexo (H ou M): ')
            idade = input('idade: ')"""

    nome = 'nome {}'.format(c)
    sexo = 'H' if (c % 2 == 0) else 'M'
    idade = 17 + c



    pessoa = type('', (object,), {'nome': nome, 'sexo': sexo, 'idade': idade})()
    listaDePessoas.append(pessoa)

somaIdade = 0
idadeAux = 0
maisVelho = ''
mulheresMenos20 = 0
for pessoa in listaDePessoas:

    somaIdade += pessoa.idade

    if idadeAux < pessoa.idade and pessoa.sexo == 'H':
        idadeAux = pessoa.idade
        maisVelho = pessoa.nome

    if pessoa.idade < 20 and pessoa.sexo == 'M':
        mulheresMenos20 += 1


print('Idade média: {}'.format(somaIdade/5))
print('Homem mais velho: {}'.format(maisVelho))
print('Número de mulheres com menos de 20 anos: {}'.format(mulheresMenos20))



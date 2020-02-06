nome = input('Digite seu nome: \n')


print(nome[:(nome.index(" ", 0) + 1)].strip())

print(nome[nome.rfind(" "):].strip())
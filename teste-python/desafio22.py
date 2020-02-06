nome = input('Digite seu nome: \n')

print(nome.upper())

print(nome.lower())

print(len(nome.strip()))
print(nome.count(" "))

print(len(nome.strip()) - nome.count(" "))


print( nome[ : (nome.index(" ") +1 )] )
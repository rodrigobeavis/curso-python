frase = input('Digite uma frase: ')
fraseSemEspaços = ''
inversoDaFrase = ''

## frase = 'APOS A SOPA'

fraseSemEspaços = frase.replace(' ', '').lower()

for caracter in reversed(fraseSemEspaços):
    inversoDaFrase += caracter
#print(inversoDaFrase)

if inversoDaFrase == fraseSemEspaços:
    print('A frase "{}" é um Palíndromo'.format(frase))
else:
    print('A frase "{}" não é um Palíndromo'.format(frase))
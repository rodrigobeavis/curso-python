frase = input('Digite um texto qualquer? \n')

print('O texto possuí  {} de caracteres "a" '.format(frase.upper().count("A")))

print('O caracter "a" aparce a primeira vez na posição {}'.format(frase.upper().index("A")))

print('O caracter "a" aparce a última vez na posição {}'.format(frase.upper().index("A", -1)))
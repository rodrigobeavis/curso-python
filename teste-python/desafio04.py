testeTipo = input('Digite algo para verificação de tipo de dado: ')

print(type(testeTipo))

print('Númerico ? ', testeTipo.isalnum())
print('Alfabetico ? ', testeTipo.isalpha())
print('ASCII Caracter ? ', testeTipo.isascii())
print('Decimal ? ', testeTipo.isdecimal())
print('É um digito? ', testeTipo.isdigit())
print('É numerico ?', testeTipo.isnumeric())
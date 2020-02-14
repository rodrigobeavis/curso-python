import cores
print('Conversão inteiros para tipos computacionais')



numero = input('Digite o número: ')

while numero.isnumeric() == False:
    numero = input('Digite o número: ')
else:
    numero = int(numero)

print('\n {} 1 {} - para Binário '.format(cores.get('az'),cores.get('l')))
print(' {} 2 {} - para Octal '.format(cores.get('am'),cores.get('l')))
print(' {} 3 {} - para Hexadecimal '.format(cores.get('ver'),cores.get('l')))
print(' {} 4 {}- para todos os tipos \n '.format(cores.get('pb'),cores.get('l')))

selecao = 0

while selecao not in (1, 2, 3, 4):
    selecao = int(input('Digite o número correspondente ao tipo de conversão: '))
else:
    if selecao == 1:
        print('Valor Binário: {}'.format(bin(numero)))
    elif selecao == 2:
        print('Valor Octal: {}'.format(oct(numero)))
    elif selecao == 3:
        print('Valor Hexadecimal: {}'.format(hex(numero)))
    elif selecao == 4:
        print('Valor Binário: {}'.format(bin(numero)))
        print('Valor Octal: {}'.format(oct(numero)))
        print('Valor Hexadecimal: {}'.format(hex(numero)))





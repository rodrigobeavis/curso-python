num = int(input('Digite um número: '))
divisores = []
string_Divisor = ''

for count in range(1, num+1):
    if num % count == 0:
        divisores.append(count)
        string_Divisor += '{}, '.format(count)
print(string_Divisor)

if (1 in divisores) and (num in divisores) and (len(divisores) == 2):
    print('O numero {} é primo. Divisores: {}'.format(num, string_Divisor[:-2]))
else:
    print('O número {} não é primo. Divisores: {}'.format(num, string_Divisor[:-2]))
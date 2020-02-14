import cores

print('Compare dois número inteiros')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O número {} é {}maior{} que {}'.format(n1, cores.get('ver'), cores.get('l'), n2))
elif n1 < n2:
    print('O número {} é {}menor{} que {}'.format(n1, cores.get('ver'), cores.get('l'), n2))
elif n1 == n2:
    print('O número {} é {}igual{} que {}'.format(n1, cores.get('ver'), cores.get('l'), n2))

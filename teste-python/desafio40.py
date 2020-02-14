nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))

media = (nota1 + nota2) / 2

print(media)

if media < 5.0:
    print('Reprovado')
elif 5.0 <= media <= 6.9:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado')

valorProduto = float(input('Digite o valor do produto: ').replace(',', '.'))

print('Selecione uma opção de pagamento \n')
tipoPagamento = int(input(' 1- à vista dinheiro \n 2- à vista cartão \n 3- 2X cartão \n 4-3x cartão \n Digite a opção: '))

if tipoPagamento == 1:
    valorProduto -= (valorProduto * 0.10)
elif tipoPagamento == 2:
    valorProduto -= (valorProduto * 0.05)
elif tipoPagamento == 3:
    valorProduto = valorProduto
elif tipoPagamento == 4:
    valorProduto += (valorProduto * 0.20)


print('Valor {0:.2f}'.format(valorProduto))
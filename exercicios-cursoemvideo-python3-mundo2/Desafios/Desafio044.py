# Enunciado: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('\n' + '='*10 + ' Condições de pagamento ' + '='*10)
print('À vista (dinheiro/cheque): 10% de desconto.')
print('À vista no cartão:          5% de desconto.')
print('Em até 2x no cartão:       preço normal.')
print('3x ou mais no cartão:      20% de juros.')
print('='*44)

produto = float(input('Informe o valor do produto: '))

av = produto - (produto * 10)/100
avc = produto - (produto * 5)/100
acresc  = produto + (produto * 20)/100

print('\n' + '='*5 + ' Valores do produto em função da forma de pagamento ' +
      '='*5)
print('R$ {:.2f}, à vista, no dinheiro ou cheque.'.format(av))
print('R$ {:.2f}, à vista, no cartão.'.format(avc))
print('R$ {:.2f}, preço normal, se parcelado em 2x no cartão.'.format(produto))
print('R$ {:.2f}, se parcelado em 3x ou mais, no cartão.'.format(acresc))

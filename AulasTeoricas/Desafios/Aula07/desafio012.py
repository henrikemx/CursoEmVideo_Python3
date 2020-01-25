# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input('Informe o valor do produto, sem desconto: '))
d = int(input('Informe o valor do desconto, em %: '))

p2 = p1 - ((p1 * d) / 100)

print('O valor do produto, com 5% de desconto, será de R$ {:.2f}'.format(p2))

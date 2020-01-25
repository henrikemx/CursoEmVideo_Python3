# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela poderá comprar

r = float(input('Informe quantos reais tem na carteira: '))
n1 = float(input('Informe o valor do dólar atual: '))

d = r // n1

print('Com a quantia disponivel voce poderá comprar até {:.2f} dólar(es)'.format(d))

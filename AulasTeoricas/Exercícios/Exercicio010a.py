# Enunciado: desenvolva um programa que converta um valor, em Dólar, para Real

print('Qual valor do produto, em Dolar, deseja converter em Real ?')
dolar = float(input('US$ '))
# dolar = float(input('Qual valor do produto deseja converter em Real ? US$ '))
real = dolar * 3.21
print('\nO valor do produto é de R$ {:.2f} (com base no valor do Dólar em R$ 3,21)'.format(real))

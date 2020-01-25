#Enunciado: desenvolva um programa que converta um valor, em Reais, em Dolar

real = float(input('Qual valor, em Real, deseja converter em Dólar ? R$ '))
dolar = real / 3.21
print('O valor convertido é de U$ {:.2f}'.format(dolar))

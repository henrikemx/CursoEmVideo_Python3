#####################################################################
# Josefson deseja fazer compras na China. Ela quer comprar um celular
# de USD 299,99, uma chaleira de USD 23,87, um gnomo de jardim de
# USD 66,66 e 6 adesivos de unicórnio de USD 1,42 cada um. O frete
# de tudo isso para a cidade de Rolândia, no Paraná, ficou em USD 12,34.
#
#   a. Calcule o valor total da compra em dólares.
#   b. Usando o mesmo valor do dólar do exercício anterior, calcule
#       o preço final em Reais. Lembre-se que o # valor do IOF é de 6,38 %.
#   c. Quanto ela pagou apenas de IOF?
#
#####################################################################

print('Itens a serem adquiridos por Josefa da China:'
      ''''\n----------------------------------------------
1. Celular:                        US$ 299,99
2. Chaleira:                       US$  23,87
3. Gnomo de Jardim:                US$  66,66
4. 6 adesivos de Unicórnio (cada): US$   1,42
      ''')
print('Valor do frete:                    US$  12,34')

# Declarando as variáveis e seus valores...
cel = 299.99
chal = 23.97
gnomo = 66.66
advUni = 1.42
totadvUni = advUni * 6
totCompra = cel + chal + gnomo + totadvUni
cotDolar = 3.25

taxaIOF = totCompra * 6.38/100
totCompraR = (totCompra + taxaIOF) * cotDolar

print('#'*50)
print(f'O valor total da compra será de US$ {totCompra:.2f}')

print(f'Valor do Dólar: R$ \033[32m{cotDolar}\033[0;0m')
print('Valor do IOF: \033[33m6,38%\033[0;0m')
print(f'O valor final da compra, já convertido e acrescido do IOF\n'
      f'ficará em: R$ \033[34m\033[1m{totCompraR:.2f}\033[0;0m')
print(f'Josefa irá pagar, só de IOF sobre essa compra, R$ \033[31m{taxaIOF:.2f}\033[0;0m')

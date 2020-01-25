##################################
# exemplo de código de exibição da
# sequencia de Fibonacci extraído
# da documentçção do Python 2.8.0
##################################

print('*' * 40)
# declarando as variáveis...
a, b = 0, 1

# lógica de desenvolvimento da sequencia...

while a < 1000:
    print(a, end=', ') # será exibido enquanto a condição for verdadeira
    a, b = b, a+b
print('Fim...')

print('*' * 40)

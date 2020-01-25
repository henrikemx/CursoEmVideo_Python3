# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = int(input('Digite o valor, em metros: '))

c = m * 100
m = m * 1000

print('O resultado foi de {} centimetros e {} milimetros'.format(c, m))

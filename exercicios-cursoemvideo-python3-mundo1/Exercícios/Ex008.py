# Enunciado: desenvolva um programa que leia um numero digitado, em metros, e o exiba em milimetros,
# centimetros, decimetros, decametros e quilometros.

num = float(input('Digite o valor para o qual desejar ver toda sua faixa: '))
print('{} metro(s) vale {} milimetros'.format(num, num*1000))
print('{} metro(s) vale {} centímetros'.format(num, num*100))
print('{} metro(s) vale {} decimetros'.format(num, num*10))
print('{} metro(s) vale {} decametros'.format(num, num/10))
print('{} metro(s) vale {} hectometros'.format(num, num/100))
print('{} metro(s) vale {} quilometros'.format(num, num/1000))

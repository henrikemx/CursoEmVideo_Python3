# Enunciado: desenvolva um programa que leia um numero inteiro e mostre na tela se ele é IMPAR ou PAR.

num = int(input('\nInforme o numero: '))

resultado = num % 2

if resultado == 0:
    print('\nO numero {} é PAR !!'.format(num))
else:
    print('\nO numero {} é IMPAR !!'.format(num))

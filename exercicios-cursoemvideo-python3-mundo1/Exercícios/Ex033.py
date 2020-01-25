# Enunciado: faça um programa que leia 3 numeros e mostre qual deles é o MAIOR e qual é o MENOR

n1 = int(input('\nInforme o 1º numero: '))
n2 = int(input('Informe o 2º numero: '))
n3 = int(input('Informe o 3º numero: '))

if n3 < n1 > n2 :
    print('\nO numero {} é o MAIOR.'.format(n1))
if n3 < n2 > n1:
    print('\nO numero {} é o MAIOR.'.format(n2))
if n2 < n3 > n1:
    print('\nO numero {} é o MAIOR.'.format(n3))
if n3 > n1 < n2:
    print('O numero {} é o MENOR.'.format(n1))
if n3 > n2 < n1:
    print('O numero {} é o MENOR.'.format(n2))
if n2 > n3 < n1:
    print('O numero {} é o MENOR.'.format(n3))

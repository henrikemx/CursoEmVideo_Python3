# Enunciado: faça um programa que leia um ano qualquer e mostre se ele é BISEXTO.

ano = int(input('\nInforme o ano: '))

ano1 = ano % 4
ano2 = ano % 100

if ano1 == 0 and ano2 != 0:
    print('\nO ano de {} é Bissexto !!'.format(ano))
else:
    print('\nO ano de {} não foi Bissexto !!'.format(ano))

# Enunciado: desenvolva um programa que leia o ano de nascimento de 7 pessoas
#  e, no final, quantas delas ainda não atingiram a maioridade (21 anos) e,
# destas, quantas são maiores.

from datetime import date

menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1

if menor > 0:
    print('\nDestas, {} pessoa(s) tem menos de 21 anos !'.format(menor))

if maior > 0:
    print('\nDestas, {} pessoa(s) tem mais de 21 anos !!'.format(maior))

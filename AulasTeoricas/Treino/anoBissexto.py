# Enunciado: faça um programa que leia um ano qualquer e mostre se ele é BISEXTO.

while True:
    ano = int(input('\nInforme o ano: '))

    ano1 = ano % 4
    ano2 = ano % 100
    ano3 = ano % 400

    if ano1 == 0 and ano2 != 0 or ano3 == 0:
        print('\nO ano de {} é Bissexto !!'.format(ano))
    else:
        print('\nO ano de {} não foi Bissexto !!'.format(ano))
    print('='*30)
    resp = str(input('Deseja continuar ? [S/N] '))
    if resp in 'Nn':
        break
print(f'\n{" FIM DO PROGRAMA ":=^30}')
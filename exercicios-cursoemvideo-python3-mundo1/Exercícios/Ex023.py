#Enunciado: faça um programa que leia um numero de 0 a 9999 e mostre, na tela, cada um dos digitos separados.

#Ex.: Digite um numero

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

sel = str(input('\nInforme um numero, de 0 a 9999: '))

tam = len(sel)

if tam == 1:
    print('\nUnidade: {}'.format(sel))
if tam == 2:
    print('\nUnidade: {}'.format(sel[1]))
    print('Dezena: {}'.format(sel[0]))
if tam == 3:
    print('\nUnidade: {}'.format(sel[2]))
    print('Dezena: {}'.format(sel[1]))
    print('Centena: {}'.format(sel[0]))
if tam == 4:
    print('\nUnidade: {}'.format(sel[3]))
    print('Dezena: {}'.format(sel[2]))
    print('Centena: {}'.format(sel[1]))
    print('Milhar: {}'.format(sel[0]))

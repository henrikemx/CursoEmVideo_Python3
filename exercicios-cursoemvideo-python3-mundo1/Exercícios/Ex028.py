# Enunciado: escreva um programa que 'pense' em um numero de 0 a 5 e peça ao usuário para tentar descobrir qual foi o numero escolhido pelo computador.

# O programa devera escrever, na tela, se o usuário ganhou ou perdeu.

from random import randint
from time import sleep

cpu = randint(0, 5)

print('#' * 20)
print('Jogo da adivinhação')
print('#' * 20)
print('Aguarde, estou escolhendo um numero...')
sleep(3)

user = int(input('\nQual numero eu escolhi ? '))

if user == cpu:
    print('\nParabéns, voce acertou !')
else:
    print('\nInfelizmente voce não acertou. Tente novamente !')

print('\nO computador escolheu o numero {} !'.format(cpu))
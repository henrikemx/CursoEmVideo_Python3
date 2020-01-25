# Desafio 58: melhore o jogo do Desafio 028, onde o computador vai 'pensar' em
# um numero de 0 a 10. Só que agora, o jogador vai ter que adivinhar até acertar
# mostrando,no final, quantos palpites foram ncessários para vencer.

# Abaixo segue o código desenvolvido no desafio 28 já modificado

from random import randint
from time import sleep

print('#' * 20)
print('Jogo da adivinhação')
print('#' * 20)
print('Aguarde, estou escolhendo um numero...')
sleep(3)

user = int(input('\nQual numero eu escolhi ? '))
cpu = randint(0, 11)
cnt = 1

while user != cpu:
    user = int(input('\Infelizmente voce não acertou. Tente novamente ! => '))
    cnt += 1

print('\nParabéns, voce acertou !')
print('\nEu escolhi o numero {} !'.format(cpu), end=' ')
print('Voce realizou {} tentativas até acertar !'.format(cnt))

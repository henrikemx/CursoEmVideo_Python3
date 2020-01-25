'''
Enunciado: desenvolva um programa que ajude um jogador da MegaSena a criar palpites.

O programa deverá perguntar qtos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo (sem repetir números), cadastrando tudo em uma única lista composta.
'''

from random import randint
from time import sleep

ms = []
nj = 0

print('-'*40)
print(f'{" JOGOS DA MEGA SENA ":^40}')
print('-'*40)

nj = int(input('Qtos jogos voce quer que eu sorteie ? '))

print()

for cnt in range(nj):
    for c in range(6):
        num = randint(1, 60)
        if num not in ms:
        	ms.append(num)
        else:
        	num = randint(1, 60)
        	ms.append(num)
    ms.sort()
    print(f'Jogo {cnt+1}: {ms}')
    sleep(1)
    ms.clear()

'''
Enunciado: desenvolva um programa que ajude um jogador da MegaSena a criar palpites.

O programa deverá perguntar qtos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo (sem repetir números), cadastrando tudo em uma única lista composta.
'''

from random import randint
from time import sleep

# definindo as variáveis

lista = []
jogos = []
quant = 0
tot = 1

print()
print(f'{" Gerador de MegaSena ":=^34}')

quant = int(input('Quantos jogos deseja gerar ? '))

# definindo a lógica dos sorteios

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort() # deixa em ordem crescente
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print()
print('='*7, f' SORTEANDO {quant} JOGOS ', '='*7)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

print()
print(f'{" BOA SORTE !! ":=^34}')
print()
print(f'{" FIM DO PROGRAMA ":=^34}')

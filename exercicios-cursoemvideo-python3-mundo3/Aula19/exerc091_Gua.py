'''
Enunciado: desenvolva um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

ranking = []

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print('-'*30)
print('=> Valores sorteados: ')
print('-'*30)

for k, v in jogo.items():
    print(f' - {k} tirou o valor {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-'*30)
print(f'{" RANKING DOS JOGADORES ":=^30}')
print('-'*30)

for i, v in enumerate(ranking):
    print(f' - {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

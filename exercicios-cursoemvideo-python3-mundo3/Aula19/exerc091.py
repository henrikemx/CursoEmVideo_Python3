'''
Enunciado: desenvolva um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero
no dado.
'''

# ================================================ #
from random import randint
from time import sleep

# ================================================ #
# definindo as variaveis

jogo = {}
lista = []
maior = 0
pos = 0

# ================================================ #
# gerando um dicionario com numeros aleatorios de 1 a 6

jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)

print('-'*30)

# ================================================ #
print('Resultado dos sorteios:')
print('-'*30)
for k, v in jogo.items():
    print(f'  O {k} sorteou o nº {v}')
    sleep(1)
#print(f'{" Fim do Sorteio ":=^30}\n')

# ================================================ #
# definindo a lógica do sorteio dos ganhadores

cnt = 0
for e in jogo.items():
    if cnt == 0 or e[1] <= maior:
        maior = e[1]
        lista.append(e)
    else:
        while pos < len(lista):
            if e[1] >= lista[pos][1]:
                lista.insert(pos, e)
                break
            pos += 1
    cnt += 1

print(f'\n{" RANKING DOS GANHADORES ":=^30}')
print('-'*30)

for c, l in enumerate(lista):
    print(f'  {c+1}º Lugar: {l[0]} com {l[1]}')
    sleep(1)

print(f'\n{" Fim do Sorteio ":=^30}')

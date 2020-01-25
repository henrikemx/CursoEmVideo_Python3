'''
Enunciado: desenvolva um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No
final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}
gols1 = []
gols2 = {}
total = cnt = 0

jogador['nome'] = str(input('\nNome do jogador: '))
for c in range(0, 5):
    gols = int(input(f'Quantos gols na partida {c} ? '))
    total += gols
    gols1.append(gols)
    cnt += 1
jogador['gols'] = gols1
jogador['total'] = total
print('='*30)

print(f'O jogador {jogador["nome"]} jogou {cnt} partidas.')
print('-'*30)

totgols = 0
for e in jogador.items():
    if e[0] == 'gols':
        for i, v in enumerate(e[1]):
            print(f'  => Na partida {i}, fez {v} gols.')
            totgols += v

print(f'Foi um total de {totgols} gols.')

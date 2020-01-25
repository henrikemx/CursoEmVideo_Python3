'''
Enunciado: desenvolva um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No
final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

# coding = utf-8

# definindo as variáveis
jogador = dict()
partidas = list()

# entrando com os dados...
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))

# loop para inserir o numero de gols na lista...
for c in range(0, tot):
    partidas.append(int(input(f' => Quantos gols na partida {c+1} ? ')))

jogador['gols'] = partidas[:] # copia o conteúdo da lista no dicionario...
jogador['total'] = sum(partidas) # soma o total de gols na lista...

print('='*30)
print(jogador) # exibe o conteudo do dicionario...
print('='*30)

# loop para exibir o conteudo do dicionario...
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('='*30)

# exibe o nome e o total de gols feitos...
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

# loop para exibir o conteudo da lista dentro do dicionario...
for i, v in enumerate(jogador['gols']):
    print(f' => Na {i+1}ª partida fez {v} gols.')

# Exibe o total de gols em todas as partidas
print(f'\nFoi um total de {jogador["total"]} gols.')

print(f'\n{" FIM DO PROGRAMA ":=^30}')
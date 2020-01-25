'''
Enunciado: desenvolva um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No
final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

# coding = utf-8

# definindo as variáveis
time = list()
jogador = dict()
partidas = list()

# entrando com os dados...
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))

    # loop para inserir o numero de gols na lista...
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' => Quantos gols na partida {c+1} ? ')))

    jogador['gols'] = partidas[:] # copia o conteúdo da lista no dicionario...
    jogador['total'] = sum(partidas) # soma o total de gols na lista...
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! Digite apenas S ou N')
    if resp == 'N':
        break
print('*'*40)

print('cod ', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print()

print('-'*40)

for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-'*40)

while True:
    busca = int(input('Buscar dados de qual jogador ? (999 Encerra) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO ! Não existe jogador com esse código {busca}...')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')

        for i, g in enumerate(time[busca]["gols"]):
            print(f' ==> No jogo {i+1} fez {g} gols')

    print('-' * 40)

print('<<< ENCERRADO >>>')
'''
Enunciado: aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
'''

jogador = {}
jogadores = []
gols = []
gol = []
total = tot = 0

while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    for c0 in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {c0} ? ')))
        jogador['gols'] = gol.copy()
        for c1 in range(0, len(gol)):
            tot += gol[c1]
            jogador['total'] = tot
        tot = 0
        if len(gol) == partidas:
            jogadores.append(jogador.copy())
            gol.clear()
    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        break

# print(jogadores)

print('-' * 35)
print(f'{"Cod":<5}{"Nome":<10}{"Gols":12}{"Total":^5}')
print('-' * 35)

for c, e in enumerate(jogadores):
    print(f'{c:<5}{e["nome"]:<10}{e["gols"]}{e["total"]:^8}')
print('-' * 35)

while True:
    idx = int(input('Mostrar dados de qual jogador ? [999 para Sair] '))
    print('-' * 30)
    if idx == 999:
        break
    if idx > len(jogadores) - 1:
        print('Erro !! Não existe esse índice...')
        continue
    print('-- LEVANTAMENTO DO JOGADOR:', jogadores[idx]['nome'])
    for c, d in enumerate(jogadores[idx]['gols']):
        print(f'   No jogo {c} fez {d} gols.')
    print('-' * 30)

print(f'{" Fim do programa ":=^30}')

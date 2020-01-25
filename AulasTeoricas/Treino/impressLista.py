jogadores = [{'nome': 'Nelson', 'gols': [0, 2, 1], 'total': 3}, {'nome': 'Mario', 'gols': [2, 1, 3], 'total': 3}]
tot = 0
idx = 1

print('-'*35)
print(f'{"Cod":<5}{"Nome":<10}{"Gols":12}{"Total":<5}')
print('-'*35)

for c, e in enumerate(jogadores):
    print(f'{c:<5}{e["nome"]:<10}{e["gols"]}{e["total"]:>8}')
print('-'*35)

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


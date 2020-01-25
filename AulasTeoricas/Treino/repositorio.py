'''
    print('-- LEVANTAMENTO DO JOGADOR', jogadores[c]['nome'])
    print('-'*30)
    while idx == c:
        for v in jogadores:
            print(v)
    print('-'*30)

'''


'''
for c, e in enumerate(jogadores):
    #print(f'{c:<5}{e["nome"]:<10}{e["gols"]}')
    for v in e.values():
        #print(e)
        print(v[0])
'''
'''
for c, e in enumerate(jogadores):
    for v in e.values():
        print(f'v = {v}')
        if type(v) == str:
            print(v)
            nome = v
        if type(v) == list:
            print(len(v))
            for c in range(len(v)):
                tot += v[c]
            print(tot)
'''
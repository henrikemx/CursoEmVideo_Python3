print()
from random import randint
lista = []
maior = pos = 0
jogo = {}

jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)

for e in jogo.items():
    if len(lista) == 0 or e[1] > lista[0][1]:
        lista.append(e)
    else:
        for cnt in range(0, 4):
            while pos < len(lista):
                print('cnt =', cnt, end=', ')
                print('pos =', pos, ', len(lista) =', len(lista))
                print('lista[cnt][1] =', lista[cnt][1])
                if e[1] <= lista[cnt][1]:
                    lista.insert(pos, e)
                    break
            pos += 1
print('='*30)
print(lista)



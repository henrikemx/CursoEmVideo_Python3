word = str(input('\nEscreva uma palavra qualquer: '))
cnt = 0

for c in word:
    cnt += 1
    print(c, end='')
print('\nA palavra que voce digitou tem {} letras.'.format(cnt))

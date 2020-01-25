# Desafio 61: refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao

cnt = 0
seq = 0

print('\nA PA de {} é: '.format(termo), end='')
while cnt < 10:
    print(termo, end=' => ')
    termo += razao
    cnt += 1
print('Acabou !!')

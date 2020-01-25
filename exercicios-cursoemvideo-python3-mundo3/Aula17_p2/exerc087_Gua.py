'''
Enunciado: aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor na segunda linha;
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

spar = scol = mai = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c}: '))
print('='*30)

# lógica para calculo da soma dos valores pares

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print('='*30)
print(f'A soma dos valores pares é {spar}')

# lógica para calcular a soma dos valores na 3ª coluna

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores na 3ª coluna é {scol}')

# lógica para calculo dos valores na 2ª linha

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor na 2ª linha é {mai}')

print(f'{" Fim do programa ":=^30}')

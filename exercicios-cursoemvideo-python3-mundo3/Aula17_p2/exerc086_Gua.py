'''
Enunciado: desenvolva um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No
final, mostre, na tela, a matriz com a formatação correta.
'''

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))

print()
print('*-*' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:>5}]', end='')
    print()

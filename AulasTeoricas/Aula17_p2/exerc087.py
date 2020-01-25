'''
Enunciado: aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor na segunda linha;
'''

mat = [0] * 3
par = valor = col3 = lin2 = mai = 0

for x in range(3):
    mat[x] = [0] * 3

for lin in range(3):
    for col in range(3):
        mat[lin][col] = int(input(f'Informe um valor para a posição [{lin}, {col}]: '))
        valor = mat[lin][col]
        if valor % 2 == 0:
            par += valor

print('*-*' * 15)
for lin in range(3):
    for col in range(3):
        print(f'[{mat[lin][col]}]', end='')
        if col == 2:
            col3 += mat[lin][col]
            print()
        if lin == 1 and col == 0:
            mai = mat[lin][col]
        elif lin == 1 and (col > 0 or col < 2):
            if mat[lin][col] > mai:
                mai = mat[lin][col]
print('*-*' * 15)
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {col3}')
print(f'O maior valor na segunda linha é: {mai}')

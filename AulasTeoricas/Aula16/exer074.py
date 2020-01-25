'''
Enunciado: crie um programa que gere 5 números aleatórios e colocar em uma
tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
'''

# desenvolvendo a lógica para gerar numeros aleatórios
# módulo random
# referencia: aula 08 do mundo 1

from random import randint

maior = 0
menor = 0

print(f'Os numeros gerados foram: ', end='')
for c in range(0, 5):
    num = randint(1, 10)
    print(num, end=' ')

    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('\n')
print(f'O maior numero sorteado foi: {maior}')
print(f'O menor numero sorteado foi: {menor}')


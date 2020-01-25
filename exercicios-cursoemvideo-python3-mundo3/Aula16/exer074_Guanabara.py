'''
Enunciado: crie um programa que gere 5 números aleatórios e colocar em uma
tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
'''

'''
A solução abaixo foi mostrada no vídeo de 30/05
'''

# desenvolvendo a lógica para gerar numeros aleatórios
# módulo random
# referencia: aula 08 do mundo 1

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\nOs números sorteados foram: ', end='')

for n in num:
    print(f'{n} ', end=' ')
print('\n')

print(f'O maior número sorteado foi o {max(num)}')
print(f'O maior número sorteado foi o {min(num)}')
print('\n')

'''
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
'''

# Enunciado: Faça um programa que tenha uma lista chamada numeros e 2 funções chamada sorteio() e somaPar().
# A primeira função irá ser responsável por sortear 5 números e vai colocá-los dentro de uma lista e a segunda função
#  irá mostrar a soma entre todos os valores PARES sorteados pela função anterior.

# Inicio do programa
from time import sleep
from random import randint

# definir as funções
def sorteia(lista):
    print('Sorteando os números: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('\nFim do sorteio !!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista} é igual a {soma}')

# primeiro passo... criar uma lista
numeros = list()
sorteia(numeros)
somaPar(numeros)

#print(numeros)

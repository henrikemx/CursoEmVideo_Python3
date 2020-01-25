# Enunciado: desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem, ou não, formar um triangulo

r1 = float(input('\nInforme o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))

from math import hypot, radians

# Testando qual reta é a maior

if r2 < r1 > r3:
    print('\nO numero {} é o maior.'.format(r1))
    hi = r1
if r1 < r2 > r3:
    print('\nO numero {} é o maior.'.format(r2))
    hi = r2
if r2 < r3 > r1:
    print('\nO numero {} é o maior.'.format(r3))
    hi = r3

# Testando qual reta é a menor

if r2 > r1 < r3:
    print('\nO numero {} é o menor.'.format(r1))
    co = r1
if r1 > r2 < r3:
    print('\nO numero {} é o menor.'.format(r2))
    co = r2
if r1 > r3 < r2:
    print('\nO numero {} é o menor.'.format(r3))
    co = r3

# Calculando o valor da outra reta

ca = int((hi**2 - co**2) ** (1/2))
print('\nO valor da outra reta deverá ser de {}.'.format(ca))

if ca == r1 or ca == r2 or ca == r3:
    print('\nEstas retas podem gerar um triangulo.')
else:
    print('\nEstas retas não podem formar um triangulo.')

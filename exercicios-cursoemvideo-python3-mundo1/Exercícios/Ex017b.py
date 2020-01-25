'''Enunciado: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot
print('\nO exemplo a seguir usará a importação...')
print('A hipotenusa é a raiz quadrada da soma do quadrado do cateto oposto e do cateto adjacente\n')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\nO valor da hipotenusa é de {:.2f}'.format(hi))

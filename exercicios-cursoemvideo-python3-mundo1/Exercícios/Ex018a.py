'''Enunciado: Faça um programa que leia um ângulo qualquer e mostre, na tela, o valor do seno, cosseno e tangente desse ângulo.

Coseno: É a razão entre o cateto adjacente e a hipotenusa de um triângulo retângulo, conforme a Lei dos Cossenos.
Fórmula: Cos = Cateto adjacente / hipotenusa

Seno: É a razão entre o cateto oposto e a hipotenusa de um triângulo retângulo, conforme a Lei dos Senos.
Fórmula: Sen = Cateto oposto / hipotenusa

Tangente: É a razão entre o cateto oposto e o cateto adjacente de um triângulo retângulo.
Fórmula: Tan = Cateto oposto / Cateto adjacente

Cateto oposto = linha vertical
Cateto adjacente: linha horizontal
Hipotenusa = linha que diagonal dentro de um triângulo retângulo
'''

import math
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hi = math.sqrt((math.pow(co, 2) + math.pow(ca, 2)))
print('O valor da hipotenusa é de {}'.format(hi))
print('\nConvertendo Radianos em Graus...')
seno = co / hi
dg = math.trunc(math.degrees(math.sin(seno)))
print('O valor do ângulo correspondente ao seno é de {}'.format(dg) + ' Graus')
cos = ca / hi
dg1 = math.trunc(math.degrees(math.cos(cos)))
print('\nO valor do ângulo correspondente ao cosseno é de {}'.format(dg1) + ' Graus')
tang = co / ca
dgt = math.ceil(math.degrees(math.tan(tang)))
print('\nO valor da tangente é de {}'.format(tang))
print('O valor do ângulo da tangente é de {}'.format(dgt) + ' Graus')

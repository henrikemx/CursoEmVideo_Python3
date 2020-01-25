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

from math import radians, sin, cos, tan
angulo = float(input("Informe o valor do ângulo: "))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tag = tan(radians(angulo))
print('\nO Seno de {} Graus é de {:.2f}\no Cosseno é de {:.2f} \ne a Tangente é de {:.2f}'.format(angulo, seno, cos,
                                                                                                 tag))

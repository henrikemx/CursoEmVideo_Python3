'''Enunciado: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''

print('O exemplo a seguir usará o método tradicional)'
print('A hipotenusa é a raiz quadrada da soma do quadrado do cateto oposto e do cateto adjacente')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 1/2
print('O valor da hipotenusa é de {:.2f}'.format(hi))

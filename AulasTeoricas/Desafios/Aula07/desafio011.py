# Faça um programa que leia a largura e altura de uma parede, em metros, calcule a sua áreae a quantidade de tinta
# necessária para pinta-la, sabendo que cada lata de tinta pinta uma área de até 2 m2

l = float(input('Informe a largura, em metros: '))
a = float(input('Informe a altura, em metros: '))
m2 = l * a
lt = m2 / 2

print('Uma parede com essas medidas irá consumir {} latas de tintas !'.format(int(lt)))

# Enunciado: desenvolva um programa que, com base na altura e largura de uma parede, em metros, calcule sua
# área e apresente a quantidade de litros de tinta necssários  para pintá-la, sabendo que o gasto médio é
# de 1 litro de tinta para cada 2 m2.

largura = float(input('Digite a largura da parede, em metros: '))
altura = float(input('Digite a altura da parede, em metros: '))
area = largura * altura
litros = area / 2
print('Será necessário {:.2f} litros de tinta para pintar uma parede de {:.2f} m2'.format(litros, area))

# Enunciado: Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('\nInforme o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos podem gerar um triangulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Trata-se de um \033[33mTRIANGULO EQUILÁTERO.\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Trata-se de um \033[33mTRIANGULO ISÓSCELES\033[m')
    else:
        print('Trata-se de um \033[33mTRIANGULO ESCALENO\033[m')
else:
    print('\nOs segmentos não podem formar um triangulo.')

import math
print('\nExercicio executado de duas formas distintas...\n')
num = float(input('Informe o numero: '))
print('\nA primeira é importando no formato padrão (import math)')
print('\n1. O numero {} tem a parte inteira igual a {}'.format(num, math.trunc(num)))

from math import trunc
print('\nA segunda é importando no formato padrão (from math import trunc)')
print('\n1. O numero {} tem a parte inteira igual a {}'.format(num, trunc(num)))

print("\nOutra forma de mostrar a porção inteira seria usando a função 'int(num)' no lugar de 'math.trunc(num)' ou 'trunc(num)'")
print('\n3. O numero {} tem a porção inteira igual a {}'.format(num, int(num)))

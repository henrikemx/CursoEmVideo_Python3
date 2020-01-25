print('Calcule o resto da divisão de 10 por 3')
print(f'10 % 3 = {10 % 3}')
print('='*30)
print('Calcule a tabuada do 3')
# nesse exemplo é necessário o uso de loop for
n = 3
for f in range(0, 11):
    print(f'{n} * {f} = {n * f}')
print('='*30)
print('Davinir não gosta de ir às aulas, mas ele é obrigado a comparecer a pelo menos 75% delas.')
print('Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana,\n durante quatro meses. Ajude o Davinir!')
# declarar as variáveis
aulasMes = 2 * 4
totAulas = aulasMes * 4
tAulas = totAulas * 0.25
print(f'Se o curso de Davinir dura 4 meses, sendo de 2 aulas/semana, o curso tem, no TOTAL, {totAulas} aulas\n e ele '
      f'precisa comparecer a 75% delas, pelo menos,\n então Davinir pode faltar a {tAulas} aulas.')
print('='*30)
from math import pi
print('Calcule a área de um círculo de raio 𝑟 = 2.')
print('Lembrete: a área de um círculo de raio 𝑟 é: 𝐴∘ = 𝜋 𝑟2')
print(f'A área total de um círculo de raio igual a 2 é {pi * 2 ** 2:.6f}')
print('='*30)

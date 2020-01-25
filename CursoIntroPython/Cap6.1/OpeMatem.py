# Operadores matemáticos, recapitualação

print('-'*30)
print('Exemplos de operações matemáticas em Python...')
print('-'*30)
n1 = int(input('Informe 1º número: '))
n2 = int(input('Informe 2º número: '))
n3 = int(input('Informe o valor da raiz: '))

print('-'*30)
print(f'Soma: {n1} + {n2} = {n1+n2}')
print(f'Subtração: {n1} - {n2} = {n1-n2}')
print(f'Divisão: {n1} / {n2} = {n1 / n2}')
print(f'Multiplicação: {n1} * {n2} = {n1 * n2}')
print(f'Potenciação: {n1} elevado a {n3} = {n1 ** n3}')
print(f'Raiz de {n2} é {n2**(1/n3):.3f}')
print(f'Divisão Inteira: {n1} // {n2} = { n1 // n2}')
print(f'Resto da divisão: {n1} % {n2} = {n1 % n2}')

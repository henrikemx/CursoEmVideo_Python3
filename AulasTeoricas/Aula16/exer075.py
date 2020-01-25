'''
Enunciado: desenvolva um programa que leia 4 valores e guarde-os em uma tupla.
No final:

A) quantas vezes apareceu o valor 9
B) em que posição foi digitado o primeiro valor 3
C) quais foram os números pares
'''

'''
As dicas a seguir foram extraídas do link: http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_09.html#numeros-aleatorios

a) Para criar uma tupla com um único elemento, temos que incluir uma vírgula final
b) Sem a vírgula, Python entende ('a') como uma string entre parênteses
'''

# montando a estrutura solicitada pela primeira parte do enunciado:

n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor: '))
n3 = int(input('Informe o 3º valor: '))
n4 = int(input('Informe o 4º valor: '))

n = (n1,) + (n2,) + (n3,) + (n4,)

print(f'Os números digitados foram: {n}')

# uma vez gerada a tupla, segue desenvolver a lógica que atenda as condições A, B e C

# A) quantas vezes apareceu o valor 9

# testar se o numero 9 foi digitado em algum momento

n9 = n.count(9)
if n9 == 0:
    print(f'\nA) O número 9 não aparece nenhuma vez')
else:
    print(f'\nA) O número 9 aparece {n.count(9)}x')

# B) em que posição foi digitado o primeiro valor 3

print(f'\nB) O número 3 aparece na {n.index(3)}ª posição')

# C) quais foram os números pares

for c in range(0, 3):
    print(n[c])
    ++c

#    if par % 2:
#        pares = (n,)

print(f'\nC) Os números pares digitados foi(ram): {pares}')

print('Fim do programa')

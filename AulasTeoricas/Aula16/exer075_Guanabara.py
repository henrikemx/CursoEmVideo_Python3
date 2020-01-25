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

num = (int(input('Informe o 1º valor: ')),
       int(input('Informe o 2º valor: ')),
       int(input('Informe o 3º valor: ')),
       int(input('Informe o 4º valor: ')))

print(f'\nOs números digitados foram: {num}')

# uma vez gerada a tupla, segue desenvolver a lógica que atenda as condições A, B e C

# A) quantas vezes apareceu o valor 9

print(f'\nO número 9 foi digitado {num.count(9)} vezes')

# testar se o numero 9 foi digitado em algum momento

# B) em que posição foi digitado o primeiro valor 3

# durante o vídeo, Guanabara implementou uma solução para os casos em que
# o usuário não digite o valor 3

if 3 in num:
    print(f'\nO número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('\nO valor 3 não foi digitado nenhuma vez')

# C) quais foram os números pares

print('\nOs valores pares digitados foi(foram): ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')

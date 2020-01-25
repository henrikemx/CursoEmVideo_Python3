'''
Enunciado: crie um programa que leia vários valores e coloque-os em uma lista. Depois disso, mostre:

A) quantos números foram digitados.
B) a lista de valores, ordenada de forma decrescente.
C) se o valor 5 foi digitado e está ou não na lista.
'''

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print()
print('-='*40)
print(f'A) Voce inseriu {len(valores)} numeros !')
valores.sort(reverse=True)
print(f'B) Voce inseriu os seguintes numeros, em ordem decrescente: {valores}')
if 5 in valores:
    print('C) O valor 5 está na lista !')
else:
    print('C) O valor 5 não está na lista !')
print('-='*40)

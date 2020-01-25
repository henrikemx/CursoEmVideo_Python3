'''
Enunciado: faça um programa que leia 5 valores numeŕicos e guarde-os em uma lista.
No finla, mostre qual o maior e menor valor digitado e suas respectivas posições na lista.
'''

valores = list()
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Informe um valor para a posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print()
print(f'Voce digitou os números: {valores}')

print(f'\nO maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')

print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()
print(f'\n{" Fim de Programa ":*^40}')
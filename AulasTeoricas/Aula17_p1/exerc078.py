'''
Enunciado: faça um programa que leia 5 valores numeŕicos e guarde-os em uma lista.
No finla, mostre qual o maior e menor valor digitado e suas respectivas posições na lista.
'''

valores = list()
maior = 0
menor = 0
pmaior = []
pmenor = []

for c in range(0, 5):
    valores.append(int(input(f'Informe um valor para a posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
            pmaior.append(c)
        if valores[c] < menor:
            menor = valores[c]
            pmenor.append(c)

print()
print(f'Voce digitou os números: {valores}')

'''
print(f'\nO maior valor foi {maior} na posição ', end='')
for cnt1 in range(0, len(pmaior)):
    print(f'{pmaior[cnt1]}...', end='')

print(f'\nO menor valor foi {menor} na posição ', end='')
for cnt2 in range(0, len(pmenor)):
    print(f'{pmenor[cnt2]}...', end='')
'''
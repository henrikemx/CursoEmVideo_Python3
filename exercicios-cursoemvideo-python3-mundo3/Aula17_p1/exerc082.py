'''
Enunciado: crie um programa que leia vários números e coloque-os em uma lista.

Depois, crie duas listas extras que contenham, apenas, os valores pares e ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das 3 listas geradas.
'''

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Informe um valor: ')))
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
lista.sort()
par.sort()
impar.sort()

print()
print('-='*20)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
print('-='*20)

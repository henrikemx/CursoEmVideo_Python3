# Enunciado: desenvolve um programa que leia o primeiro termo e a razão de
# uma PA e, no final, mostre os 10 primeiros termos dessa progressão

# Progressão aritmética:
# An = A1 + (n-1)r
# An = termo geral
# A1 = primeiro termo
# n = numero de termos
# r = razão da PA

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao

print('\nA PA de {} é igual a: '.format(termo), end='')
for c in range(termo, decimo + razao, razao):
    print('{:2}'.format(c), end=' -> ')
print(' Acabou !!')

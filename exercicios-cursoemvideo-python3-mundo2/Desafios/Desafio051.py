# Enunciado: desenvolve um programa que leia o primeiro termo e a razão de
# uma PA e, no final, mostre os 10 primeiros termos dessa progressão

# Progressão aritmética:
# An = A1 + (n-1)r
# An = termo geral
# A1 = primeiro termo
# n = numero de termos
# r = razão da PA

termo = int(input('Informe o primeiro termo: '))
num = int(input('Informe o numero de termos: '))
razao = int(input('Informe a razão: '))

for c in range(1, num + 1):
    pa = termo + (c-1)*razao
    print('A PA do {:2}º termo é igual a {:2}'.format(c, pa))

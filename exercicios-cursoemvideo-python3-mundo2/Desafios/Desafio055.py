# Enunciado: desenvolva um programa que leia o peso de 5 pessoas e, no final,
#  mostre qual foi o maior e o menor peso lidos

maior = -10 ** 20
menor = 10 ** 20

for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
        
print('O maior peso informado foi de {:.2f}'.format(maior))
print('O menor peso informado foi de {:.2f}'.format(menor))

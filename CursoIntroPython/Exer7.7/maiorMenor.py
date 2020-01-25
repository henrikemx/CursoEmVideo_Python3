#################################################
# Este script pertence ao Desafio nº 55 do Curso
# de Python 3, mundo 2. Nele é solicitado que seja
# desenvolvido um programa que leia o peso de 5
# pessoas e, no final, mostre qual foi o maior
# e o menor peso lidos
#################################################

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print()
print(f'O maior peso informado foi de {maior:.1f} Kg')
print(f'O menor peso informado foi de {menor:.1f} Kg')

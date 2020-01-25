# estrutura de pesquisa de maior e menor valores

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print()
print('O maior peso informado foi de {:.1f} Kg'.format(maior))
print('O menor peso informado foi de {:.1f} Kg'.format(menor))

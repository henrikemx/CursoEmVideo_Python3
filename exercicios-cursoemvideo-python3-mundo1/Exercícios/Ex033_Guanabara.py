print('\n====== Solução nº 1 ======')

distancia = float(input('\nQual a distancia de sua viagem ? '))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print('\nO preço de sua passagem será de R$ {:.2f}.'.format(preço))

print('\n====== Solução nº 2 ======')

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('\nO preço de sua passagem será de R$ {:.2f}.'.format(preço))


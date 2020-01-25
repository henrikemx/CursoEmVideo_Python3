# Enunciado: desenvolva um programa que pergunte a distancia de uma viagem, em km. Calcule o preço da passagem, cobrando R$ 0,50/km para viagens de até 200 km e de R$ 0,45/km para viagens acima de 200 km.

dist = float(input('\nInforme a distancia: '))

if dist < 200:
    print('\nVoce irá gastar R$ {:.2f} com a passagem !!'.format(dist * 0.5))
else:
    print('\nVoce irá gastar R$ {:.2f} com a passagem !!'.format(dist * 0.45))

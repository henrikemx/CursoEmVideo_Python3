#Enunciado: Crie um programa que leia o nome de uma cidade e diga se ela começa, ou não, com a palavra "SANTO"

cidade = str(input('\nInforme o nome da cidade: '))

pal = cidade.upper().find('SANTO')

if pal == 0:
    print('\nA cidade possui SANTO no nome !')
if pal != 0:
    print('\nA cidade não possui SANTO no nome')

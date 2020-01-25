#Enunciado: crie um programa quwe leia o nome de uma pessoa e diga se ela tem, ou não, "SILVA" no nome.

nome = str(input('\nInforme o nome: ')).strip()

#nome1 = nome.lower().find('Silva')

if 'silva' in nome.lower():
    print('\nEsta pessoa tem SILVA no nome !')
else:
    print('\nEsta pessoa não tem SILVA no nome !')

print('\n=== Abaixo, segue a solução do Guanabara ===\n')

#nome = str(input('Qual o seu nome completo ?' ))

print('Seu nome tem Silva ? {}'.format('silva' in nome.lower()))

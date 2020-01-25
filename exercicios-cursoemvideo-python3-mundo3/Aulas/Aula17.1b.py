# exemplo de criação de listas à partir da declaração de uma função

'''há 2 formas de definir uma lista:

valores = []

ou

valores = list()
'''

valores = []

# atribuindo valores a essa lista

valores.append(5)
valores.append(9)
valores.append(4)
print(f'A) O conteudo da lista "valores" é: {valores}')

# outra forma de exibir essa lista de forma mais "elegante"

print(f'B) O conteudo da lista "valores" é: ', end='')
for v in valores:
    print(f'{v}...', end=' ')

# nesse outro exemplo será exibido tanto a posição quanto seu conteudo

print()
print(f'C) Conteúdo exibido em forma de listagem: ')
print('='*28)
for c, v in enumerate(valores):
    print(f'A posição {c} contém o valor {v}')
print('='*28)
print(f'Fim da Lista !!')
print()

# no exemplo a seguir será adiconado valores à lista pelo teclado

del valores
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))
print(f'D) Os valores digitados foram: {valores} ou...')
print(f'E) Conteúdo exibido em forma de listagem: ')
print('='*28)
for c, v in enumerate(valores):
    print(f'A posição {c} contém o valor {v}')
print('='*28)
print(f'Fim da Lista !!')
print()

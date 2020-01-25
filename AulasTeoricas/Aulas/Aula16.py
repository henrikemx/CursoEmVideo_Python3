'''
lanche = ('Hamburger','Suco','Pizza','Pudim','Batata Frita')
# Tuplas são imutáveis
#lanche[1] = 'Refrigerante'

# Uma forma de exibir a lista

# for comida in lanche:
#    print(f'Eu vou comer {comida}')
# print('\nUfa !! Comi pra caramba !!')

# Outra forma de exibir a lista
'''

'''
for cont in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[cont]}')
print('\nUfa !! Comi pra caramba !!')
'''

# Outras formar de apresentação de resultado

'''
print()
for cont in range(0,len(lanche)):
    print(f'Elemento {lanche[cont]} no índice {cont}')
print('='*30)

print('Outra forma de codificar com mesmo resultado...\n')
for pos, comida in enumerate(lanche):
    print(f'Elemento {comida} está no índice {pos}')
print('='*30)
'''
'''
# Para organizar os itens em uma tupla podemos usar a função 'sorted'

print()
print(f'Lista de itens para o lanche: {sorted(lanche)}')
'''

'''
a = (2, 5, 4)
b = (5, 8, 1 ,2)
c = b + a

# print(len(c))
# print(c.count(5))
print()
print(c)
print(c.index(4))
'''

pessoa = ('Gustavo', 39, 'M', 98.99)
print('\n', pessoa)

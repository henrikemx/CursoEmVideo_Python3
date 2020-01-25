# outra forma de declaração de listas

a = [2, 3, 4, 7]
b = a
print(f'Conteudo da lista A: {a}')
print(f'Conteudo da lista B: {b}')

print('='*80)
b[2] = 8
print(f'Aqui foi atribuido o valor 8 à posição 2 da lista B...')
print(f'Conteudo da lista A: {a}')
print(f'Conteudo da lista B: {b}')
print('='*80)
print(f'No exemplo acima, Guanabara explica que o Python cria uma ligação entre as 2 listas, motivo pelo qual')
print(f'qualquer alteração no conteudo da lista B se reflete na lista A')
print('='*80)
print(f'À seguir, Guanabara mostra que existe um forma de se criar uma cópia de uma lista...')
print(f'Nesse caso é empregada a técnica de fatiamento...')
del a, b
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print('='*80)
print(f'Exibindo o conteudo do código...')
print('''
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
''')
print(f'À seguir, como ficaram as listas após aplicação da técnica de fatiamento...')
print(f'Aqui foi atribuido o valor 8 à posição 2 da lista B...')
print(f'Conteudo da lista A: {a}')
print(f'Conteudo da lista B: {b}')
print(f'Alteração realizada com sucesso...')
print('='*80)

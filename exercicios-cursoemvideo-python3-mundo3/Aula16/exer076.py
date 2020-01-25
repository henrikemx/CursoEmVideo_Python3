'''
Enunciado: crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequencia.

No final, nostre uma listagem de preços, organizando os dados em forma tabular.
'''

#l = 'LISTA DE PREÇOS'
print()
print('-'*40)
#print(f'{l:^40}')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
# abaixo desse comentário ficará o código que irá exibir a lista
# contida na tupla
lp = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,'Estojo',
      25.00,'Transferidor', 4.20,'Compasso', 9.99,'Mochila', 120.32,
      'Canetas', 22.30,'Livros', 34.90)

for pos, lista in enumerate(lp):

    #print(f'{lista}, contador {pos}')
    if pos % 2 == 0:
        print(f'{lista:.<30}', end='')
    else:
        print(f' R${lista:>7.2f}')
print('-'*40)

# abaixo, solução do Gustavo

'''
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
'''

'''
Enunciado: crie um programa onde o usuário possa digitar 5 valores numeŕicos e cadastre-os em uma lista,
já na posição correta de inserção (sem o uso do sort()).

No final, mostre a lista ordenada na tabela.
'''

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista !')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista !')
                break
            pos += 1

print()
print('-='*30)
print(f'Os valores inseridos, na ordem crescente, foram: {lista}')
print('-='*30)
print()
print(f'{" FIM DO PROGRAMA ":=^40}')

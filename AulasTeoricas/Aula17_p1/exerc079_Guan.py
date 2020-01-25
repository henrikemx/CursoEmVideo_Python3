'''
Enunciado: crie um programa onde um usuário possa digitar vários valores numeŕicos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''

# solução apresentada pelo Guanabara durante a aula

num = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso !')
    else:
        print('Valor duplicado ! Não será adicionado !')

    r = str(input('Deseja continuar ? [S/N] '))
    if r in 'Nn':
        break

print()
print('-='*20)
num.sort()
print(f'Os valores inseridos foram: {num}')
print('-='*20)
print()
print(f'{" FIM DO PROGRAMA ":=^30}')
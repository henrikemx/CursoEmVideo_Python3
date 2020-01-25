'''
Enunciado: desenvolva um programa que leia o nome e as 2 notas de vários alunos e guarde tudo em uma única lista
composta. No final, mostre um boletim, formatado, contendo a média de cada aluno e que permita, ao usuário,
exibir as notas de cada aluno, individualmente.
'''

from time import sleep
ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'nN':
        break
print()
print('='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)

while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno ? (999 para parar) '))
    if opc == 999:
        print('Finalizando...')
        sleep(1)
        break
    if opc <= len(ficha) - 1:
        print('-'*30)
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    if opc > len(ficha) - 1:
        print('Erro !!! Não existe aluno com esse índice !!')
        continue
print()
print(f'{" FIM DO PROGRAMA ":=^30}')



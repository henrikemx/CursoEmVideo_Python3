'''Enunciado: O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos.

Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

'''
a1 = str(input('Digite o primeiro nome do aluno: '))
a2 = str(input('Digite o segundo nome do aluno: '))
a3 = str(input('Digite o terceiro nome do aluno: '))
a4 = str(input('Digite o quarto nome do aluno: '))
'''

from random import shuffle

'''Jogaremos o nomes digitamos em uma lista'''
lista = ['Andre','Luiz','Carlos','Maria']

'''Seguindo a lógica do Guanabara'''
shuffle(lista)
print('\n=== Segue a lista dos sorteados ===\n')
print('1º aluno(a): {}'.format(lista[0]))
print('2º aluno(a): {}'.format(lista[1]))
print('3º aluno(a): {}'.format(lista[2]))
print('4º aluno(a): {}'.format(lista[3]))

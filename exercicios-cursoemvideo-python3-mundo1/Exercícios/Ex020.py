'''Enunciado: O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos.

Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

a1 = input('Informe o nome do 1ª aluno: ')
a2 = input('Informe o nome do 2ª aluno: ')
a3 = input('Informe o nome do 3ª aluno: ')
a4 = input('Informe o nome do 4ª aluno: ')

lista = [a1, a2, a3, a4]

shuffle(lista)

print('\nA ordem de apresentação será:')
print(lista)

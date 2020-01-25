'''Enunciado: Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import randint
a1 = input('Informe o nome do 1º aluno: ')
a2 = input('Informe o nome do 2º aluno: ')
a3 = input('Informe o nome do 3º aluno: ')
a4 = input('Informe o nome do 4º aluno: ')

sorteio = randint(1, 4)

if (sorteio == 1) :
    print('O aluno escolhido é: {}'.format(a1))
if (sorteio == 2) :
    print('O aluno escolhido é: {}'.format(a2))
if (sorteio == 3) :
    print('O aluno escolhido é: {}'.format(a3))
if (sorteio == 4) :
    print('O aluno escolhido é: {}'.format(a4))
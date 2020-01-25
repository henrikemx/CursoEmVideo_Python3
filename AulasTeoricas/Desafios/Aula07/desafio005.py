# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um valor: '))
a = n1 - 1
p = n1 + 1
print('O numero anterior a {} é {}'.format(n1, a))
print('O numero posterior a {} é {}'.format(n1, p))

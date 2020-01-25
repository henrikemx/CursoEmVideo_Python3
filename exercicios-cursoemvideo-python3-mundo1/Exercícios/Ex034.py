# Enunciado: escreva um programa que pergunte qual o salário de um funionário e que calcule o valor do seu aumento. Condição: para salários acima de R$ 1250,00 calcule um aumento de 10% e para salários inferiores, um aumento de 15%

sal = float(input('\nInforme o salário do funcionário: R$ '))

if sal < 1250:
    print('\nO salário, com aumento de 10%, passará a ser de R$ {:.2f}'.format(sal * 1.1))
else:
    print('\nO salário, com aumento de 15%, passará a ser de R$ {:.2f}'.format(
        sal * 1.15))

# Desafio: desenvolva um programa que, com base no valor atual do salário, exiba seu valor com 15% de aumento

print('Informe o valor atual do seu salário:')
salario = float(input('R$ '))
novosalario = salario + (salario * 15/100)
print('\nO novo valor, com aumento de 15%, será de R$ {:.2f}'.format(novosalario))

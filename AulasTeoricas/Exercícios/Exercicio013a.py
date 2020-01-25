# Desafio: desenvolva um programa que exiba o novo valor do salário informado com base em uma porcentagem informada

print('Informe o valor atual do seu salário:')
salario = float(input('R$ '))
# print('\nInforme a porcentagem de aumento proposto:')
porcentagem = float(input('\nInforme a porcentagem de aumento proposto: '))
novosalario = salario + (salario * porcentagem/100)
print('\nO novo valor, com aumento de {} %, será de R$ {:.2f}'.format(porcentagem, novosalario))

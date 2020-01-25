# Enunciado:
#
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder a 30% do salario ou então o emprestimo sera negado.

imovel = float(input('Qual o valor do imóvel ? '))
salario = float(input('Qual o valor do salário ? '))
anos = int(input('Quantos anos de financiamento ? '))

prest = imovel/anos
limite = (salario * 30) / 100

print(
    '\nPara financiar um imóvel de R$ {:.2f} em {} prestações, cada prestação '
    'sairá por R$ {:.2f}.'.format(
        imovel, anos, prest))

if prest > limite:
    print('\nFinanciamento RECUSADO !')
    print('Voce só poderá comprometer até R$ {:.2f} do seu salário.'.format(
        limite))
else:
    print("\nParabéns! Finaniamento APROVADO !.")

# Enunciado: faça um algoritmo que leia o preço de um produto e mostre seu novo valor, com o desconto de 5%

preco = float(input('Qual o valor do produto ? R$ '))
novo = preco - (preco * 5/100)
print('Este produto que custava R$ {:.2f}, com o desconto de 5%, passa a custar R$ {:.2f}'.format(preco, novo))
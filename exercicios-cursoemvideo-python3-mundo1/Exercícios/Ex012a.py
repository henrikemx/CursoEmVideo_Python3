# Enunciado: faça um algoritmo que leia o preço de um produto e mostre seu novo valor, com o desconto de 5%

preco = float(input('Qual o valor do produto ? R$ '))
desconto = float(input('Qual o valor dado de desconto, em % ?? '))
novo = preco - (preco * desconto/100)
print('Este produto que custava R$ {:.2f}, com o desconto de {} %, passa a custar R$ {:.2f}'.format(preco, desconto, novo))

# print('O valor inserido no campo desconto foi {:.2f}'.format(desconto))

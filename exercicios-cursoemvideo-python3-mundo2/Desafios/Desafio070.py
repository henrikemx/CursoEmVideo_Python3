# Desevolva uma aplicação qe leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário deseja, ou não, encerrar o programa. Ao encerrar, o programa deverá apresentar, na tela:

from builtins import str

# A) Qual o total gasto na compra
# B) Qtos produtos custaram mais de R$ 10.000,00
# C) Qual foi o produto mais barato

print('='*30)
print('{:^30}'.format(' Loja Super Baratão '))
print('='*30)

total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Informe o produto: '))
    preco = float(input('Informe o preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
    
print('{:-^40}'.format(' Fim do Programa '))
print()
print(f'O total gasto foi de R$ {total:.2f}')
if totmil != 0:
    print(f'Há {totmil} produto(s) que custou(ram) mais de R$ 1.000,00')
print(f'E o(a) {barato} foi o produto mais barato e custa R$ {menor:.2f}')
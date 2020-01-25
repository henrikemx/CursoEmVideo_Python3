# Enunciado: desenvolva um programa que tenha uma função chamada área() que receba as dimensões de um terreno
# retangular (largura x comprimento) e mostre a qual a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} m x {comp} m é de {a:.2f} m²')

# programa principal

print(' Cálculo de área ')
print('-' * 20)

# entrada de dados

l = float(input('Informe o valor da largura (m): '))
c = float(input('Informe o valor do comprimento (m): '))

# função a ser chamada
area(l, c)

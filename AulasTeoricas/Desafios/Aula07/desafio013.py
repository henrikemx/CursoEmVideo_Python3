# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

si = float(input('Informe o valor do salário atual: '))
a = int(input('Informe o percentual de aumento: '))

# au = (si * a)/100
nv = si + ((si * a)/100)

print('O salário reajustado será de R$ {:.2f}'.format(nv))

# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um valor: '))

d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)

print('O dobro de {} é {}'.format(n1, d))
print('O triplo de {} é {}'.format(n1, t))
print('E a raiz quadrada de {} é {:.3f}'.format(n1, rq))

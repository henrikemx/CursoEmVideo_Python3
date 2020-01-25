# Enunciado: desenvolva um programa que gere a tabuada do numero digitado na tela

num = int(input('Digite o numero para geração da Tabuada: '))
print('-' * 12)
n = 0
for c in range(0, 10):
        n += 1
        print('{} * {:2} = {}'.format(num, n, num*n))
print('-' * 12)

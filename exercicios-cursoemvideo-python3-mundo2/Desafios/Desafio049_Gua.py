# Enunciado: desenvolva um programa que gere a tabuada do numero digitado na tela

num = int(input('Digite o numero para geração da Tabuada: '))
print('-' * 12)
for c in range(1, 11):
        print('{} * {:2} = {}'.format(num, c, num*c))
print('-' * 12)

# Enunciado: desenvolva um programa que leia um numero inteiro e informe se
# ele é, ou não, um numero PRIMO, isto é, divisível por 1 e por ele mesmo

cont = 0
num = int(input('Informe um numero: '))
print('O numero informado é divisível por: ')
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print(c, end=' ')
if cont <= 2:
    print('\nLogo, {} é um numero PRIMO !'.format(num))
else:
    print('\nPortanto, {} não é um numero PRIMO !'.format(num))

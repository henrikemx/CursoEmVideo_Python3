# Desafio 60: desenvolva um programa que leia um numero qualquer e mostre o seu
# fatorial. Ex.:5! = 1x2x3x4x5 = 120

num1 = int(input('Informe o numero que deseja fatorar: '))
fat = 1
cnt = num1

print('\n{}! = '.format(num1), end='')

while cnt >= 1:
    print(cnt, end='')
    if cnt != 1:
        print(' x ', end='')
    fat *= cnt
    cnt -= 1
print(' = {}'.format(fat))

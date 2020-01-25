from random import randint

maior = 0
menor = 0

print(f'Os numeros gerados foram: ', end='')
for c in range(0, 5):
    num = randint(1, 10)
    print(num, end=' ')

    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('\n')
print(f'O maior numero sorteado foi: {maior}')
print(f'O menor numero sorteado foi: {menor}')

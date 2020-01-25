# Enunciado: desenvolva um programa que leia 6 numeros inteiros e mostre,
# na tela, somente a soma daqueles que forem pares, ignorando os ímpares.

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Informe um numero qualquer: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont > 1:
    print('\nA soma dos {} numeros pares é igual a {}'.format(cont, soma))
elif cont == 1:
    print('\nVoce informou somente 1 numero par.\nPortanto o resultado é {'
          '}'.format(soma))
else:
    print('\nVoce não informou nenhum numero par !!')
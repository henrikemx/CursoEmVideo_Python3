# Desafio 59: desenvolve um programa que leia 2 numeros e, em seguida, mostre
# um menu na tela. Esse programa deverá realizar a operação solicitada em cada
#  caso - vide figura anexa.

num1 = int(input('\nInforme o 1º numero: '))
num2 = int(input('Informe o 2º numero: '))

soma = mult = maior = menor = novo = sair = 0

print('''\nEscolha a opção desejada:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa''')

opcao = int(input('\nOpção: '))

while sair != 5:
    if opcao == 1:
        soma = num1 + num2
        print('\nA soma de {} e {} = {}'.format(num1, num2, soma))
        sair = 5
    if opcao == 2:
        mult = num1 * num2
        print('\nO resultado de {} x {} = {}'.format(num1, num2, mult))
        sair = 5
    if opcao == 3:
        if num1 > num2:
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1
        print('\n{} é maior que {} !'.format(maior, menor))
        sair = 5
    if opcao == 4:
        print('\nEscolha os novos numeros')
        num1 = int(input('\nInforme o 1º numero: '))
        num2 = int(input('Informe o 2º numero: '))
        opcao = int(input('\nSelecione a opção: '))
    if opcao == 5:
        sair = 5

print('\nFim do programa !!')




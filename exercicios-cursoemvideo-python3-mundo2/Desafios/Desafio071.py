# Simulador de Cx Eletronico
from builtins import int

# Desenvolva uma aplicação que simule as operações de um caixa eletronico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

# Obs.: considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e R$ 1,00

print('='*40)
print('{:*^40}'.format(' Banco CEV '))
print('='*40)
valor = int(input('Qual o valor deseja sacar ? \n==> R$ '))
print()
print('Serão entregues os seguintes valores: ')
print()
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced:>2} de R$ {ced:>2}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print()
print('{:*^40}'.format(' Obrigado e Volte Sempre !! '))
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função 'input()' do Python,
# só que fazendo a 'validação' para aceitar apenas valores numéricos.

# Ex.:
# n = leiaInt('Digite um n')
#-------------------------------------------------------------------
# o código abaixo foi desenvolvido durante o exercício...

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro ! digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# aqui vai o programa principal
n = leiaInt('Digite um núemro: ')
print(f'Voce acabou de digitar o número {n}')

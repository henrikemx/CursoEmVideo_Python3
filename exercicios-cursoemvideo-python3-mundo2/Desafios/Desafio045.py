# Enunciado: crie um programa que faça o computador jogar Jokenpô com voce

# Regra do Jokenpo:

print('\n' + '='*10 + ' Que forma vence o que ' + '='*10)

print('Pedra   ganha da tesoura (quebra a tesoura)')
print('Tesoura ganha do papel   (corta o papel)')
print('Papel   ganha da pedra   (embrulha a pedra)')
print('='*43)

from random import randint
import os

cntjog = 0
cntcpu = 0
parar = 'S'

while parar.upper() == 'S':
    
    # Lógica do jogo #
    
    print('\n' + '='*5 + ' Faça sua escolha ' + '='*5)
    print('1. Pedra')
    print('2. Tesoura')
    print('3. Papel')
    print('='*28)

    jog = int(input('\nFaça sua escolha: '))

# Lógica do jogador #

    if jog == 1:
        print('\nO Jogador escolheu \033[35mPEDRA\033[m')
    elif jog == 2:
        print('\nO Jogador escolheu \033[36mTESOURA\033[m')
    else:
        print('\nO Jogador escolheu \033[32mPAPEL\033[m')

# Lógica do computador #

    cpu = randint(1, 3)

    if cpu == 1:
        print('O Computador escolheu \033[35mPEDRA\033[m')
    elif cpu == 2:
        print('O Computador escolheu \033[36mTESOURA\033[m')
    else:
        print('O Computador escolheu \033[32mPAPEL\033[m')

# Lógica do jogo #

    if jog != cpu:
        if (jog == 1 and cpu == 2) or (jog == 2 and cpu == 3) or (jog == 3 and
                                                                      cpu == 1):
            cntjog += 1
            print('O Jogador \033[1;34mVENCEU\033[m !')
        else:
            cntcpu += 1
            print('O Computador \033[1;34mVENCEU\033[m')
    else:
        print('\033[31mEMPATE\033[m !!')

    parar = str(input('\nDeseja continuar ? [S/N] '))
    print('\n'*20)
    
# Lógica do placar #

print('\n' + '='*5 + ' Placar Final ' + '='*5)
print('Computador {} x {} Jogador'.format(cntcpu, cntjog))

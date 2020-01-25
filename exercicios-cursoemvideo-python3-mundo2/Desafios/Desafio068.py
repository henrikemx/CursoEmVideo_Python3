# Desenvolva uma aplicação para jogar PAR ou IMPAR com o computador. A condição para encerrar o programa deverá ser quando o usuário PERDER, exibindo o número de vitórias consecutivas !!

from random import randint
from builtins import int, str

vit = 0
print('='*10, ' Game PAR ou IMPAR ', '='*10)
while True:
    jogador = int(input('Informe um valor [0 a 5]: '))
    if jogador > 5:
        print('Número inválido. Reinicie o jogo !!')
        break
    computador = randint(0, 5)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR/IMPAR [P/I]: ')).strip().upper()[0]
    print(f'\nVoce jogou {jogador} e o computador {computador}, total de {total}', end = ' ')
    print('(Deu PAR !!)' if total % 2 == 0 else '(Deu IMPAR !!)')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce GANHOU !!')
            vit += 1
        else:
            print('Voce PERDEU !!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce GANHOU !!')
            vit += 1
        else:
            print('Voce PERDEU !!')
            break
    print('\nVamos jogar novamente...')
print()
if vit == 0:
    print(f'Voce não teve nenhuma vitória !!')
else:
    print(f'Voce ganhou {vit} partida(s) !!')
print('='*15, ' Fim do Game ', '='*15)
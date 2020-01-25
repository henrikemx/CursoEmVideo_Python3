# Faça um programa que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o 'nome' de um jogador e
# quantos 'gols' ele marcou.
# O programa deverá ser capaz de mosrar a 'ficha do Jogador', mesmo que algum dado não tenha sido iformado corretamente.
#--------------------------------------------------------------------
# o código abaixo foi desenvolvido durante o exercício...

def ficha(jogo = '<desconhecido>', gol = 0):
    print(f'O jogador {jogo} fez {gol} gol(s) no campeonato.')

# programa principal
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)
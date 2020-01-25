# Desenvolve uma aplicação que exiba a tabuada de vários números, um por vez, para cada valor digitado. A condição prara o encerramento do programa será quando o usuário entrar com um valor negativo.

from builtins import int

print('='*15, ' Gerador de Tabuada ', '='*15, '\n')
while True:
    n = int(input('Informe o número: '))
    if n < 0:
        break
    print('='*30)
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n*c:>3}')
    print('='*30)
print()
print('='*15, ' Fim do Programa ', '='*15)
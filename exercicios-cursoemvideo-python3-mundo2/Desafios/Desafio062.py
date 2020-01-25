# Desafio 62: melhore o desafio 061, perguntando ao usuário se ele deseja que
# seja exibido mais algum termo. O programa deverá encerrar quando ele disser
# que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

cnt = 0


print('\nA PA de {} é: '.format(termo), end='')
while cnt < 10:
    print(termo, end=' => ')
    termo += razao
    cnt += 1
    if cnt == 10:
        cont = str(input('Acabou !! \nDeseja continuar ?? [S/N]  ')).strip().upper()
        if cont == 'S':
            termo = int(input('Informe o novo termo: '))
            razao = int(input('Informe a nova razão: '))
            print('\nA PA de {} é: '.format(termo), end='')
            cnt = 0
print('Fim do programa !!')
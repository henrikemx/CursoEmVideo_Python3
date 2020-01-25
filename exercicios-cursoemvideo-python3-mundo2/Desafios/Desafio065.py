# Desafio 65: desenvolva um programa que leia vários numeros inteiros pelo
# teclado. No final da execução, mostre a média entre todos os valores e qual
# foi o 'maior' e o 'menor' valores lidos. O programa deve perguntar ao usuário
# se ele quer, ou não, continuar a digitar valores.

# Obs.: para chegar a uma solução foi usado como referencia o codigo do
# desafio 055

num1 = media = maior = menor = cnt = soma = 0
sair = 'N'

while sair != 'S':
    num1 = int(input('Informe um valor qualquer inteiro: '))
    sair = str(input('Deseja encerrar o programa ? [S/N]  ')).strip().upper()[0]
    if sair not in 'SsNn':
        print('Opção inválida. Favor informe se "S ou N"!!')
        sair = str(input('\nOpção: '))
        if sair not in 'SsNn':
            print('\nAbortando programa por não atender a exigência...')
            sair = 'S'
    soma += num1
    cnt += 1
    media = soma / cnt
    if cnt == 1:
        maior = num1
        menor = num1
    else:
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1
    
print('\nResultados:\nA média dos valores informados é de {}.\nO maior valor '
      'foi '
      'de {}.\nO menor valor foi de {}'.format(media, maior, menor))

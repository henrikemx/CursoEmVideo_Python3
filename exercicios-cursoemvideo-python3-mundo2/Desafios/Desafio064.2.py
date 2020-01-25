# Desafio 64: desenvolva um programa que leia vários numeros inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos numeros foram digitados e qual
# foi a soma entre eles (desconsiderando o FLAG).

cnt = soma = total = salvo = num1 = 0

while num1 != 999:
    num1 = int(input('Informe um numero qualquer: '))
    cnt += 1
    soma += num1
    if num1 == 999:
        salvo = cnt - 1
        soma -= num1
        cnt = 999
        print('\nFim do ciclo !')
print('\nVoce informou {} numeros ao sistema e a soma desses numeros é de {'
      '}'.format(salvo, soma))


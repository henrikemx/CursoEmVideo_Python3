# Crie um programa que leia diversos numeros inteiros pelo teclado. O programa só deverá encerrar quando o usuário digitar 999, que é a condição de parada. Ao fnalizar a aplicação, deverá ser exibido quantos numeros foram digitados  e qual foi o resultado da soma entre eles (desconsiderando o FLAG).


cont = soma = 0
while True:
    num = int(input('Digite um valor inteiro [999 para encerrar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
# print()
print(f'\nVoce entrou com {cont} números e a soma dos valores é de {soma} !!')
print()
print('='*15, ' Fim do Programa ', '='*15)
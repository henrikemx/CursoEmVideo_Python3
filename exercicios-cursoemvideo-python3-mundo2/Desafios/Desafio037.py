# Enunciado:

# Escreva um programa que leia um numero inteiro qualquer e peça ao usuario para escolher quel sera a base de conversao:

# 1 para Binario
# 2 para octal
# 3 para hexadecimal

num = int(input('Informe o numero que deseja converter: '))
print('''
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input('\nSelecione a base de conversão: '))

if escolha == 1:
    print('\nO numero {} em Binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('\nO numero {} em Octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('\nO numero {} em Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida\033[m !!')
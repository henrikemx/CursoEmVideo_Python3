# Enunciado:
# Esreva um programa que leia 2 numeros inteiros e compare-os, mostrando, na tela, uma mensagem:

# O primeiro valor e maior
# O segundo valor e maior
# Não existe valor maior, os dois são iguais

num1 = int(input('Informe o 1º numero: '))
num2 = int(input('Informe o 2º numero: '))

if num1 > num2:
    print('\n{} é maior que {}'.format(num1,num2))
elif num1 < num2:
    print('\n{} é maior que {}'.format(num2, num1))
else:
    print('\nAmbas as entradas são iguais !!!')

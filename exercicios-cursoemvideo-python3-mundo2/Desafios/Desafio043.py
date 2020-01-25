# Enunciado: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# de 25 a até 30: sobrepeso
# de 30 a 40: obesidade
# acima de 40: obesidade mórbida

# Fórmula para o calculo do IMC: peso / altura ao quadrado

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

from math import sqrt

imc = peso / pow(altura,2)

print('\n' + '='*10 + ' Tabela IMC ' + '='*10)
print('IMC de até 18.5  (abaixo do peso)')
print('IMC de 18.5 a 25 (Peso ideal)')
print('IMC de 25 a 30   (Sobrepeso)')
print('IMC de 30 a 40   (Obesidade)')
print('IMC acima de 40  (Obesidade Mórbida)')
print('='*32 + '\n')

if imc < 18.5:
    print('Seu IMC é de {:.2f} e se encontra \033[31mABAIXO DO PESO\033['
          'm'.format(
        imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é de {:.2f} e está no seu \033[32mPESO IDEAL\033[m'.format(
        imc))
elif 25 < imc <= 30:
    print('Seu IMC é de {:.2f} e se encontra com \033[31mSOBREPESO\033['
          'm'.format(
        imc))
elif 30 < imc <= 40:
    print('Seu IMC é de {:.2f} e está \033[35mOBESO\033[m'.format(imc))
else:
    print('Seu IMC é de {:.2f} e sofre de \033[35mOBESIDADE '
          'MÓRBIDA\033[m'.format(
        imc))


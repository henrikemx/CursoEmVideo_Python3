# Enunciado: desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem, ou não, formar um triangulo

# Solução apresentada pelo Guanabara..

print("-="*20)
print("Analizador de Triangulos")
print("-="*20)

r1 = float(input('\nInforme o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos podem gerar um triangulo.')
else:
    print('\nOs segmentos não podem formar um triangulo.')

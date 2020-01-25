# Enunciado: desenvolva um programa que calcule a soma entre todos os numeros
#  impares que sejam multiplos de 3 e que se encontrem no intervalo de 1 a 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} numeros primos encontrados dentro da faixa é igual a {'
      '}'.format(cont, soma))

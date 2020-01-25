####################################################
# Desafio 80: desenvolver um script que crie uma
# lista ordenada, de forma crescente, com os numeros
# fornecidos pelo usuário, sem o uso do método append()
####################################################

# definição da variável...
lista = []

# definição da estrutura de decisão que irá permitir
# inserir, ler a variável, identificar se o valor
# informado pé maior ou menor que os valores dentro
# da lista para definir onde este numero será armazenado.

print('='*30)
for c in range(0, 5):
    n= int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('='*30)

print(f'Os valores digitados foram: {lista}')

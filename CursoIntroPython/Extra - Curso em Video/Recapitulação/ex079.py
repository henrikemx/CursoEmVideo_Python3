####################################################
# Desafio: desenvolver um script onde o usuário informe
# diversos números inteiros, sem limite de quantidade.
# Durante a execução, o scripto deverá perguntar ao
# usuário se o mesmo desenja encerrar a entrada de dados.
# Em caso positivo, o script deverá exibir, na tela do
# console uma lista de todos os números digitados, em
# ORDEM CRESCENTE !!!
####################################################

# o código digitado abaixo foi todo ele desenvolvido
#  durante o exercício...

# definir a variável que irá armazenar a lista de
# números informados pelo usuário...
numeros = list()

# estrutura de decisão onde se decidirá QUANDO o loop
# deverá ser encerrado...
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com SUCESSO...')
    else:
        print('Valor em DUPLICADO NÃO será adicionado...')
    resp = str(input('Encerrar ? [S/N]')).strip().upper()
    if resp in 'N':
        break
print('='*30)

# aqui, antes de apresentar os numeros, serão ordenados...
numeros.sort()

print(f'Foram digitados os seguintes valores: {numeros}')

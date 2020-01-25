'''
Enunciado: Crie uma tupla preenchida com 20 primeiros colocados na tabela do
Brasileirão, na ordem de colocação e depois mostre, na tela:

A) apenas os 5 primeiros colocados
B) os 4 últimos colocados na tabela
C) uma lista com os times em ordem alfabética
D) em que posição, na tabela, encontra-se o time da Chapecoense
'''

# gerando a tupla com os nomes dos times classificados no Brasileirão 2018

brasileirao = ('Atlético-MG','Flamengo','Corinthians','Palmeiras','Fluminense',
               'América-MG','São Paulo','Grêmio','Vasco','Internacional',
               'Botafogo','Sport','Cruzeiro','Vitória','Santos','Chapecoense',
               'Atlético-PR','Bahia','Ceará','Paraná')

# a seguir, desenvolvendo a lógica que permitirá atender às 4 exigências:

# exibir somente os 5 primeiros colocados na tabela:

print('=*'*30)
print(f'Os 5 primeiros classificados foram: {brasileirao[0:5]}')
print()

# exibir somente os 4 últimos classificados na tabela
print('=*'*30)
print(f'Os 4 últimos colocados, na tabela, foram: {brasileirao[-(len(brasileirao)-16):]}')
print()

# exibir, em ordem alfabética, todos os times na tebela
print('=*'*30)
print(f'Os times na tabela, em ordem alfabética, são: {sorted(brasileirao)}')
print()

# exibir, na tela, a posição, na tabela, do time da Chapecoense
# dica: usar o método .index() para exibir o número do índice onde está armazenao o item na tupla
print('=*'*30)
'''
outra forma de exibir a posição na tabela
print(f'O time do Capecoense está na {brasileirao.index('Chapecoense')+1}ª posição na tabela')
'''
for cont in range(0, len(brasileirao)):
    if 'Chapecoense' in brasileirao[cont]:
        print(f'O time do Chapecoense é o {cont+1}º na tabela')

'''
Enunciado: desenvolva um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) quantas pessoas foram cadastradas
B) a média de idade do grupo
C) uma lista com todas as mulheres
D) uma lista com todas as pessoas com idade acima da média

'''

pessoa = {}
grupo = []
media = total = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F] ')).strip().upper()
    idade = int(input('Idade: '))
    total += idade
    pessoa['idade'] = idade
    grupo.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if r in 'Nn':
        break

media = total / len(grupo)

# ============================================ #
print(f'{" Pessoas Cadastradas ":=^30}')
for e in grupo:
    print(e)
#    print(f' => {k}:, {v}')

print('='*30)
print(f' => O grupo tem {len(grupo)} pessoas cadastradas.')
print(f' => A média de idade é de {media:.2f} anos.')

# ============================================ #
print(' => As mulheres cadastradas foram:', end=' ')

for s in grupo:
    if s['sexo'] in 'Ff':
        print(s['nome'], end=' ')

print()

# ============================================ #
print(' => Lista de pessoas que estão acima da média:')
print('-'*30)

for p in grupo:
    if p['sexo'] in 'Mm' and p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
    if p['sexo'] in 'Ff' and p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')

print()
print('\n<< ENCERRADO >>')

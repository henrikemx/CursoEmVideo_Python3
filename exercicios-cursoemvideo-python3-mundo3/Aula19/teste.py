
grupo = [{'nome': 'Pedro', 'sexo': 'M', 'idade': 18},
         {'nome': 'Maria', 'sexo': 'F', 'idade': 16},
         {'nome': 'João', 'sexo': 'M', 'idade': 26},
         {'nome': 'Paulo', 'sexo': 'M', 'idade': 21},
         {'nome': 'Joana', 'sexo': 'F', 'idade': 22},
         {'nome': 'Ana', 'sexo': 'F', 'idade': 34},]

totidade = 0
media = 0

print()


print()

for s in grupo:
    totidade += s['idade']

media = totidade / len(grupo)

print(f' => A média de idade do grupo é de {media:.2f}')

print(' => Lista de pessoas que estão acima da média:\n')

for p in grupo:
    if p['sexo'] in 'Mm' and p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
    if p['sexo'] in 'Ff' and p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')

print()

'''
for s in grupo:
    totidade += s['idade']
    print(totidade, end=' ')
'''
estado = {}
brasil = []

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    # o método acima realiza uma cópia de um elemento...
    #estado.clear()

print(brasil)
print()

print(f'{" Exibindo sem formatação ":=^40}')
for e in brasil:
    print(e)
print()

print(f'{" Exibindo de forma formatada (1) ":=^40}')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print()

print(f'{" Exibindo de forma formatada (2) ":=^40}')
for e in brasil:
    for k, v in e.items():
        print(f'{k:<5} = {v}')
print()

print(f'{" Exibindo de forma formatada (3) ":=^40}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
print()

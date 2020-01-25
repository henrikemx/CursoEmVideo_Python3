estado = {}
brasil = []

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    # o método acima realiza uma cópia de um elemento...
    #estado.clear()

#print(brasil)

for e in brasil:
    print(e)

pessoas = {'Nome':'Gustavo', 'Sexo':'M', 'Idade':25}

print(f'Conteudo da variavel: {pessoas}')

print(f'Exibindo o conteudo da chave "Nome": {pessoas["Nome"]}')

print(pessoas['Nome'])
print(pessoas['Idade'])
print('-'*40)
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')

print()
print(f'{" Exibindo as chaves (keys) ":-^40}')
print(pessoas.keys())

print()
print(f'{" Exibindo os valores (values) ":-^40}')
print(pessoas.values())

print()
print(f'{" Exibindo os itens (items) ":-^40}')
print(pessoas.items())

# O resultado desse comando é uma composição de 1 Lista [] contendo 3 tuplas

print('='*40)
for k in pessoas.keys():
    print(k, end=' ')
print()

print('='*40)
for k in pessoas.values():
    print(k, end=' ')
print()

print('='*40)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

print('='*40)
print(f'{"Apagando Item ":^40}')
print(f'{" Antes ":=^40}')
print(pessoas.items())
del pessoas['Sexo']
print('='*40)
print()
print(f'{" Depois ":=^40}')
print(pessoas.items())
print('='*40)
print()
print(f'{" Alterando item Nome ":=^40}')
pessoas['Nome'] = 'Leandro'
print(pessoas.items())
print('='*40)
print()
print(f'{" Adicionando item ":=^40}')
pessoas['Peso'] = 98.5
print(pessoas.items())
print('='*40)
print()

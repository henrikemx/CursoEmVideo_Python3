# Criando um dicionario dentro de uma lista

Estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'}
Estado2 = {'UF':'São Paulo', 'Sigla':'SP'}

# Criando uma lista

Brasil = []

# Adicionando dicionarios dentro da lista Brasil

Brasil.append(Estado1)
Brasil.append(Estado2)

print('='*40)
print(Estado1)
print(Estado2)
print(Brasil)
print(Brasil[0])
print(Brasil[1])
print('='*40)
print(f'O conteudo de UF do Item 0 => ', Brasil[0]['UF'])
#print(Brasil[0]['UF'])
print('='*40)
print()
print(f'O conteudo de Sigla do Item 1 => ', Brasil[1]['Sigla'])
#print(Brasil[1]['Sigla'])
print('='*40)
print()


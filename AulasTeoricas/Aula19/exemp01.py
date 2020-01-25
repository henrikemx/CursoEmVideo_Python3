filme = {
    'Titulo':'Star Wars',
    'Ano':1977,
    'Diretor':'George Lucas'
}

# Nesse exemplo temos 3 elementos, também chamados de KEYS (Titulo, Ano e Diretor)

'''
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
'''

# a seguir, um exemplo de manipulação de dicionario através do 'for'

print()
for k, v in filme.items():
    print(f'O {k} é {v}')
print()

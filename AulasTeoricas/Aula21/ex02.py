def teste():
    x = 8 # aqui, x é considerado um escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal

n = 2 # aqui n é considerado um escopo global
print(f'No programa principal, n vale {n}')
teste()
print('À seguir, o Python irá apresentar mensagens de erro pois o comando print não consegue enxergar a variável x, '
      'dentro do escopo loal.')
print(f'No programa principal, x vale {x}')

# Em resumo, enquanto x só é visível pela função, n será visível tanto pela função quanto pelo comando print,
# fora da função
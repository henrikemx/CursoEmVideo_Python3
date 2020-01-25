'''
Enunciado: crie um programa tenha uma tupla com várias palavras (não usar
letras acentuadas). Depois disso, voce deve mostrar, para cada palavra, quais
são as suas vogais.
'''

# abaixo, a solução apresentada pelo Gustavo...

# Definindoas tupla

palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro','pararalelepipedo')

# Gerando o cabeçallho da listagem
print()
print('-'*50)
print(f'{"Extrator de Vogais":^50}')
print('-'*50)

# o loop abaixo irá exibir, na tela, o conteúdo de cada posição dentro da tupla
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')

# a variável 'p' pode ser tratada como uma lista e, como tal, pode ler o conteúdo de cada byte
    for letra in p:
        if letra.lower() in 'aeiou': # este recurso é usado somente para exibir somente as letras contidas entre as
        # aspas
            print(letra, end=' ') # aqui será exibido somente as letras contidas entre as aspas
print()
print('-'*50)
print('\nFim do Programa')

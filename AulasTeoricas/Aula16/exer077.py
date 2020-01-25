'''
Enunciado: crie um programa tenha uma tupla com várias palavras (não usar
letras acentuadas). Depois disso, voce deve mostrar, para cada palavra, quais
são as suas vogais.
'''

# Definindoas tuplas

vogais = ('a', 'e', 'i' , 'o', 'u')
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro','pararalelepipedo','anticonstitucionalissimamente')

# Gerando o cabeçallho da listagem
print()
print('-'*50)
print(f'{"Extrator de Vogais":^50}')
print('-'*50)

# Definindo a estrutura, a lógica de pesquisa pelas vogais nas palavras

# Primeiramente será criado dois loop for

# O primeiro loop irá exibir o conteúdo lido em uma determinada posição dentro da tupla

for pos in range(0, len(palavras)):
    palavra = str(palavras[pos]) # aqui iremos forçar a saída para string
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')

# O segundo loop irá varrer cada letra da palavra

    for c in range(0, len(palavra)):

# O terceiro loop irá efetuar a comparação do conteúdo de cada vogal armazenada na tupla "vogais" com
# cada caracter a ser lido na palavra

        for idx in range(0, len(vogais)):
            if palavra[c] == str(vogais[idx]):
# Por fim, aqui é onde será exibido o resultado da busca e comparação

                print(f'{vogais[idx]}', end=' ')
    print()

print('-'*50)
print('\nFim do Programa')

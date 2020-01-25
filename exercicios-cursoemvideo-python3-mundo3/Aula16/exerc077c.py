# Aplicando as dicas dos desafios 25 e 26 da Aula 09 do Mundo 1

vogais = ('a', 'e', 'i' , 'o', 'u')
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro','pararalelepipedo','anticonstitucionalissimamente')

print()
print('-'*50)
print(f'{"Extrator de Vogais":^50}')
print('-'*50)

for pos in range(0, len(palavras)):
    palavra = str(palavras[pos])
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')

    for c in range(0, len(palavra)):
        for idx in range(0, len(vogais)):
            if palavra[c] == str(vogais[idx]):
                print(f'{vogais[idx]}', end=' ')
    print()

print('-'*50)
print('\nFim do Programa')

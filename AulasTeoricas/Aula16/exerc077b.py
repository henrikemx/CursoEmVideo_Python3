# Dica do desafio 026 da Aula 09 do Mundo 1

frase1 = ('Adalberto')
print()
print(f'A letra "A" aparece {frase1.lower().count("a")}x em {frase1}')
print(f'A variável é do tipo {type(frase1)}')

print('-'*40)
palavras = ('Adalberto','Camilo')
for pos in range(0, len(palavras)):
    palavra = str(palavras[pos])
    print(f'A primeira variável é do tipo {type(palavras)} e a segunda do tipo {type(palavra)}')
    print(f'O conteúdo da posição {pos} é {palavra} e é do tipo {type(palavra)}')
    print(f'A palavra tem {len(palavra)} caracteres')
    print(f'A palavra {palavra} tem quantas vogais "A" ? {palavra.lower().count("o")}')
    print('-'*40)
# Enunciado: desenvolva um programa que leia uma frase qualquer e informe se
# ela é, ou não, um PALINDROMO (desconsiderando os espaços)

# Exemplos:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Escreva uma frase: '))
pali = ''.join(frase.lower().split())
# print('o conteúdo da variável pali é {}'.format(pali))
# print('A variavel tem {} caracteres.'.format(len(pali)))

pali2 = ''
for c in range((len(pali)-1), -1, -1):
    pali2 += pali[c]
# print(pali2)

if pali == pali2.lower():
    print('\nEsta frase forma um \033[34mPALINDROMO\033[m !')
else:
    print('\nEsta frase \033[31mNÃO\033[m forma um \033[34mPALINDROMO\033[m !')

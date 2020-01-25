############################################
# Nessa aula foi apresentado o conceito
# de variável composto suas 3 variantes:
# a Tupla, a Lista e o Dicionário.
#
# Abaixo foi apresentado 3 formas diferentes
# de exibir o conteúdo de uma Tupla...
############################################

# atribuindo valores a uma Tupla...
lanche = ('Hamburger','Suco','Pizza','Pudim','Batata Frita')

# primeira forma...
print('#'*20 + ' Primeira Forma ' + '#'*20 + '\n')

for cnt in range(0, len(lanche)):
    print(f'Meu lanche da tarde foi: {lanche[cnt]}, na posição {cnt}')
print()

# segunda forma...
print('#'*20 + ' Segunda Forma ' + '#'*20 + '\n')
for comida in lanche:
    print(f'Meu lanche da tarde foi: {comida}')
print()

# terceira forma...
print('#'*20 + ' Terceira Forma ' + '#'*20 + '\n')
for pos, comida in enumerate(lanche):
    print(f'Meu lanche da tarde foi: {comida}, na posição {pos}')
print()

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

# Desenvolva um programa que importe esse módulo e use algumas dessas funções.
# ----------------------------------------------------------

from moeda import dobro, metade, aumentar, diminuir

p = float(input('Digite um valor: R$ '))
print()
print(f'Um aumento de 10% de R$ {p} vai para R$ {aumentar(p, 10)}')
print(f'Uma redução de 13% de R$ {p} vai para R$ {diminuir(p, 13)}')
print(f'O dobro de R$ {p} é R$ {dobro(p)}')
print(f'A metade de R$ {p} é R$ {metade(p)}')

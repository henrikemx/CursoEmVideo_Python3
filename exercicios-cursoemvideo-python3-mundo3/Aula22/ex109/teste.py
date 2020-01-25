from ex109 import moeda

p = float(input('Digite um valor: R$ '))
print()
print(f'Um aumento de 10% de R$ {moeda.moeda(p)} vai para R$ {moeda.aumentar(p, 10, True)}')
print(f'Uma redução de 13% de R$ {moeda.moeda(p)} vai para R$ {moeda.diminuir(p, 13, True)}')
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')

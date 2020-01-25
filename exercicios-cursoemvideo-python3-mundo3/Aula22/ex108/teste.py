from ex108 import moeda

p = float(input('Digite um valor: R$ '))
print()
print(f'Um aumento de 10% de R$ {moeda.moeda(p)} vai para R$ {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Uma redução de 13% de R$ {moeda.moeda(p)} vai para R$ {moeda.moeda(moeda.diminuir(p, 13))}')
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.metade(p))}')

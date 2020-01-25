def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda = 'R$ '):
    return f'{moeda}{preco:>6.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('~' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('~' * 35)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'O dobro do preço: \t\t{dobro(preco, True)}')
    print(f'A metade do valor: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de desconto: \t{diminuir(preco, taxar, True)}')
    print('~' * 35)
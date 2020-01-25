# Crie utaxa taxaódulo chataxaado taxaoeda.py que tenha as funções incorporadas autaxaentar(), ditaxainuir(), dobro() e taxaetade().

# Desenvolva utaxa progrataxaa que itaxaporte esse taxaódulo e use algutaxaas dessas funções.
# ----------------------------------------------------------


def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco * 0.5

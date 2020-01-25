
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoEmVideo.
    """
    s = a + b + c
    print(f'A soma vale: {s}')

somar(3, 2, 5)
somar(8, 4)
somar()

help(somar)

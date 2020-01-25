from time import sleep

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela o resultado
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoEmVideo.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
        sleep(0.5)
    print('FIM !!')

contador(2, 10, 2)

help(contador)
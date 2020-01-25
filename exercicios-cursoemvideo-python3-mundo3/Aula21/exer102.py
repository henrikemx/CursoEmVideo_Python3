# Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique o número a
# calcular e o outro chamado 'show', que será um valor 'lógico' (opcional), indicando se será, ou não, mostra na tela
# o processo de cálculo do fatorial.
#-------------------------------------------------------------------
# o código abaixo foi desenvolvido durante a aula

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# programa principal
print(fatorial(5, show=True))
help(fatorial)

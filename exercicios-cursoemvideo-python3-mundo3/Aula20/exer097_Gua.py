#Enunciado: desenvolva um programa que tenha uma funcão chamada escreva() que receba um texto qualquer como
# parâmetroe mostre uma mensagem com tamanho adaptável

# área das funções
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal

escreva("Pindamonhangaba do Norte")
escreva('Curso de Python 3')
escreva('Araraquara')
escreva('Ubatuba')
escreva('Itu')

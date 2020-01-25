# Enunciado: desenvolva um programa que tenha uma função chamada contador(), que receba 3 parâmetros (inicio,
# fim e passo). Seu programa tem que realizar 3 contagens através da função criada.

# A) de 1 a 10, de 1 em 1
# B) de 10 a , de 2 em 2
# C) uma contagem personalizada

from time import sleep

# área das funções
def contador(ini, fim, pas):

    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1

    print('-' * 30)
    print(f'Contagem de {ini} a {fim} de {pas} em {pas}')

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += pas
        print('FIM !')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= pas
        print('FIM !')
    print('-' * 30)

# programa principal

contador(1, 10, 1)
contador(10, 0, 2)
print('Defina o início, o final e o passo...')

i = int(input('Inicio: '))
f = int(input('Final:  '))
p = int(input('Passo:  '))

contador(i, f, p)

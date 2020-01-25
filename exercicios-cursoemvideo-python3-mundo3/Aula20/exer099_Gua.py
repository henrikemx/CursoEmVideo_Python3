# enunciado: desenvolva um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros.

# Seu programa tem que analisar todos os valores é informar qual deles é o maior

# Programa principal
# importação de biblioteca
from time import sleep

# definindo a função
def maior(* num):
    cont = maior = 0
    print('~' * 30)
    print('Analisando os valores passados')
    for valor in num: # este laço será executado até não restarem mais valores dentro da variável 'num'
        # este laço irá exibir o conteúdo da variável valor
        print(f'{valor} ', end='', flush=True)
        # dá uma pausa de 0.5 seg entre cada caracter
        sleep(0.4)
        # a função desse laço é identificar qual o maior valor em 'valor' e atribuí-lo a variável 'maior'
        if cont == 0:
            maior = valor # armazena o valor na variavel maior
        else:
            if valor > maior: # testa o conteudo da variavel valor em busca da variavel com maior valor
                maior = valor # aqui vai armazenado o maior valor encontrado
        cont += 1

    print()
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


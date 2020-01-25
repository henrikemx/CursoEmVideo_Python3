# Enunciado:

# Faça um programa que leia o ano de nascimento de um jovem e o informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))

print('\n' + '='*5 + ' Alistamento Militar ' + '='*5 + '\n')

now = date.today()

idade = now.year - nasc

if idade < 18:
    print('Está com {} anos e não é candidato ao alistamento '
          'obrigatório.'.format(idade))
elif idade == 18:
    print('Já tem {} anos e é candidato ao alistamento militar '
          'obrigatório.'.format(idade))
else:
    print('Tem {} anos e já ultrapassou tempo para apresentação ao '
          'alistamento.'.format(idade))

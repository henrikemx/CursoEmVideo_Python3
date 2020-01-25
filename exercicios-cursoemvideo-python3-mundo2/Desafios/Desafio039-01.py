# Enunciado:

# Faça um programa que leia o ano de nascimento de um jovem e o informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))

atual = date.today().year

idade = atual - nasc

print('\n' + '='*5 + ' Alistamento Militar ' + '='*5 + '\n')

print('Quem nasceu em {} tem ou irá completar {} anos em {}.'.format(nasc,
                                                                     idade,
                                                             atual))
if idade == 18:
    print('Voce terá que se alistar, IMEDIATAMENTE !!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda não é candidato ao alistamento. Ainda falta(m) {} '
          'ano(s).'.format(saldo))
    print('Deverá se alistar em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Deveria ter se alistado há {} ano(s) !!'.format(saldo))
    print('Deveria ter se alistado em {}.'.format(ano))
else:
    print('Opção inválida. Informe a ano corretamente.')

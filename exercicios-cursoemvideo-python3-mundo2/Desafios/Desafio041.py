# Enunciado: A Confereção Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SENIOR
# Acima: MASTER

from datetime import date

nasc = int(input('\nInforme o ano de nascimento do atleta: '))

atual = date.today()

idade = atual.year - nasc

print("\n" + '='*8 + ' Confederação Nacional de Natação ' + '='*8)
print('Resultado da classificação, segundo a idade do atleta\n')

if idade <= 9:
    print('O atleta tem {} anos e pertence à categoria \033[1;33mMIRIM\033['
          'm.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e pertence à categoria \033[1;33mINFANTIL\033[m.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos e pertence à categoria \033[1;33mJUNIOR\033[m.'.format(idade))
elif 19 < idade <= 20:
    print('O atleta tem {} anos e pertence à categoria \033[1;33mSENIOR\033[m.'.format(idade))
else:
    print('O atleta tem {} anos e pertence à categoria \033[1;33mMASTER\033[m.'.format(idade))

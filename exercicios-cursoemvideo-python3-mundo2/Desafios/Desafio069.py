# Desenvolva uma aplicação que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário deseja ou não continuar. Ao final do programa, este deverá apresentar:
from builtins import int, str
from _ast import Str

# A) Qtas pessoas tem mais de 18 anos.
# B) Qtos homens foram cadastrados.
# C) Qtas das mulheres cadastradas tem menos de 20 anos.

tot18 = totM = totMenos20 = 0
print('='*10, ' Cadastro de pessoas ', '='*10)
print()
while True:
    print('-'*43)
    # print('Cadastre uma pessoa')
    print('{:^41}'.format(' Cadastre uma pessoa '))
    print('-'*43)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totMenos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print()
print('='*12, ' Fim do Programa ', '='*12)
print(f'\nTemos: \n{tot18} pessoas com mais de 18 anos')
if totM != 0:
    print(f'{totM} homens')
if totMenos20 != 0:
    print(f'{totMenos20} mulher(es) com menos de 20 anos.')
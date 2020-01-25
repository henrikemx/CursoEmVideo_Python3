'''
Enunciado: desenvolva um programa que leia Nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário. Se por acaso o CTPS for diferente de 0, o dicionário receberá, também, o ano de contratação e o
salário. Calcule a acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

cad = {}
hoje = date.today()

while True:
    cad['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    idade = hoje.year - ano
    cad['idade'] = idade
    ctps = int(input('Carteira de Trabalho (0 não tem): '))
    if ctps == 0:
        cad['ctps'] = 0
        break
    else:
        cad['ctps'] = 1234
    contr1 = int(input('Ano de Contratação: '))
    contr2 = hoje.year - contr1
    cad['contratacao'] = contr1
    cad['salario'] = float(input('Salário: R$ '))
    cad['aposentadoria'] = (contr1 + 35) - ano
    break

print('='*40)
for k, v in cad.items():
    print(f'{k} tem o valor {v}')

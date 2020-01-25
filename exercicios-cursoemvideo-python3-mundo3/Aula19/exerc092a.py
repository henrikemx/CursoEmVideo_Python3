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
    cad['idade'] = hoje.year - int(input('Ano de Nascimento: '))
    ctps = int(input('Carteira de Trabalho (0 não tem): '))
    if ctps == 0:
        cad['ctps'] = 0
        break
    else:
        cad['ctps'] = 1234
        cad['contratacao'] = int(input('Ano de Contratação: '))
        cad['salario'] = float(input('Salário: R$ '))
        cad['aposentadoria'] = cad['idade'] + (cad['contratacao'] + 35) - hoje.year
    break

print('='*40)
for k, v in cad.items():
    print(f'{k} tem o valor {v}')

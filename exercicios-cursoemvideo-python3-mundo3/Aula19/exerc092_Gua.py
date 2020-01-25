'''
Enunciado: desenvolva um programa que leia Nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso o CTPS for diferente de 0, o dicionário receberá, também, o ano de contratação e o salário. Calcule a acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: [0 não tem] '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('='*30)
print(dados)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

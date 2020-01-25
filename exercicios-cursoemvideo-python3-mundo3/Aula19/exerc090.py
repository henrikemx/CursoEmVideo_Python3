'''
Enunciado: desenvolva um programa que leia nome e média de um aluno, guardando também, a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = dict()
#aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

#print('='*30)
print()
print(f'{" SITUAÇÃO DO ALUNO ":=^30}')
#print(aluno)
for k, v in aluno.items():
    #print(f' - {k}: {v}')
    print(f' - {k:.<9}: {v:>10}')
print(f'{" FIM DO PROGRAMA ":=^30}')

print('\nEsta foi a solução apresentada por Gustavo no vídeo de 23/08/2018 !!')

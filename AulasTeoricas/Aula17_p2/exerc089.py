'''
Enunciado: desenvolva um programa que leia o nome e as 2 notas de vários alunos e guarde tudo em uma única lista
composta. No final, mostre um boletim, formatado, contendo a média de cada aluno e que permita, ao usuário,
exibir as notas de cada aluno, individualmente.
'''

alunos = []
aluno = []
alu = 0

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    r = str(input('Adicionar mais ? [S/N] '))
    if r in 'Nn':
        break
print()
print(f'{" BOLETIM / MÉDIA ":=^40}')
print('No.   Nome   Media')
print('-' * 40)
# for c in range(len(alunos)):
for c, a in enumerate(alunos):
    print(f'{c:<4} {a[0]:<8} {a[3]:>4}')

print('-' * 40)

while alu != 9999:
    alu = int(input('Mostrar notas de qual aluno ? (9999 interrompe): '))
    for c, alun in enumerate(alunos):
        if c == alu:
            print(f'\n<<< As notas de {alun[0]} são {alun[1]} e {alun[2]} >>>')
            print()

print()

print(f'{" FIM DO PROGRAMA ":=^40}')

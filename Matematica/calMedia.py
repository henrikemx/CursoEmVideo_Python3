
nome = input('Nome do aluno: ')
turma = input('Turma: ')
disciplina = input('Disciplina: ')

nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))

media = (nota1 + nota2 + nota3)/3

if media > 7:
    print(f'O aluno(a) {nome}, da turma {turma} teve a nota média de'
          f' {media:.2f} '
          f'em {disciplina} foi \033[0;31m}APROVADO\033[m !')
else:
    print(f'O aluno(a) {nome}, da turma {turma} teve a nota média de {media:.2f} '
          f'em {disciplina} foi REPROVADA !')

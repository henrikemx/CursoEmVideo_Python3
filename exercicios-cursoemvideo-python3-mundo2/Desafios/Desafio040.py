# Enunciado: crie um programa que leia duas notas e calcule sua média, mostrando, no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.o e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a primeira nota: '))

media = (nota1 + nota2) / 2

print('\n' + '='*5 + ' \033[1mResultado das notas\033[m ' + '='*5)
print('A nota média do aluno foi de: \033[34m{}\033[m\n'.format(media))

if media < 5.0:
    print('O aluno foi \033[1;31mREPROVADO\033[m.')
elif 5.0 == media or 6.9 > media:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m.')
else:
    print('O aluno foi \033[1;32mAPROVADO\033[m.')
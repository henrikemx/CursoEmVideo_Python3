# Enunciado: desenvolva um programa que leia o nome, idade e sexo de 4
# pessoas e, no final, mostre:

# 1. a média de idade do grupo
# 2. qual o nome do homem mais velho
# 3. quantas mulheres tem menos de 20 anos

totidade = 0
nomevelho = ''
homemvelho = 0
mulheres = 0

for c in range(1, 5):
   msg1 = 'Informe o nome da {}ª pessoa: '.format(c)
   msg2 = 'Informe a idade da {}ª pessoa: '.format(c)
   msg3 = 'Informe o sexo da {}ª pessoa [H/M]: '.format(c)
   
   nome = str(input(msg1)).strip()
   idade = int(input(msg2))
   sexo = str(input(msg3)).strip().lower()
   print()
   
   totidade += idade

   if idade > homemvelho and sexo == 'h':
       homemvelho = idade
       nomevelho = nome
   if idade < 20 and sexo == 'm':
       mulheres += 1

media = totidade / 4

print('A idade média do grupo é de {} anos.'.format(media))

if nomevelho == '':
    print('Não tem nenhum homem no grupo.')
else:
    print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(
        homemvelho, nomevelho))

if mulheres == 0:
    print('Não tem nenhuma mulher com menos de 20 anos no grupo.')
elif mulheres == 1:
    print('Tem somente uma mulher com menos de 20 anos no grupo.')
else:
    print('Tem {} mulheres com menos de 20 anos no grupo.'.format(mulheres))

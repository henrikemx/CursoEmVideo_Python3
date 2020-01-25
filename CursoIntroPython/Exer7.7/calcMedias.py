###########################################
# Após assistir e recapitular conceitos de 
# variável do tipo LISTA da aula 17 do Curso
# em Python do canal Curso em Video irei, à
# seguir aplicar esses conhecimentos ao exer-
# cício proposto na apostila para cálculo de
# Média Aritmética, Média Geométrica e Média
# Harmônica...
#
#   M.A. = (p1 + p2 + p3 + p4)/4
#
#   M.G. = 4V(P1 * P2 * P3 * P4)
#
#   M.H. = 4/(1/P1 + 1/P2 + 1/P3 + 1/P4)
############################################

# declaração da variável
media = []
md = []
soma = inverso = maior = menor = 0
mult = 1

# informar os avlores das notas bimestrais...
print('='*30)
for c in range(1, 5):
    media.append(float(input(f'Informe a {c}ª nota: ')))

"""
# expressão para cálculo da M.A.
# ma = (n1 + n2 + n3 + n4) / 4
# calculando a M.A.
for n in range(0, len(media)):
    soma += media[n]
ma = soma / 4

# calculando a M.G...
for n in range(0, len(media)):
    mult *= media[n]
mg = mult ** (1/4)

# calculando a M.H...
for n in range(0, len(media)):
    inverso += 1/media[n]
mh = 4 / inverso
"""

# expressão para cálculo da M.A.
# ma = (n1 + n2 + n3 + n4) / 4

# esta parte do código foi deixado mais enxuto...

# calculando a M.A.
for n in range(0, len(media)):
    soma += media[n]
    mult *= media[n]
    inverso += 1 / media[n]
ma = soma / 4
mg = mult ** (1/4)
mh = 4 / inverso

# apresentação do resultado...
print('='*30)
print(f'=> Valores obtidos de soma = {soma:.2f}, mult = {mult:.2f} e inverso = {inverso:.2f}...')
print('='*30)
print(f'=> O valor da M.A. do aluno foi de \033[33m{ma:.2f}\033[0;0m.')
print(f'=> O valor da M.G. do aluno foi de \033[33m{mg:.2f}\033[0;0m.')
print(f'=> O valor da M.H. do aluno foi de \033[33m{mh:.2f}\033[0;0m.')
print('='*30)
# antes de apresentar qual foi a MAIOR e MENOR média, será necessário
# atribuit os valores a uma lista...
md = [ma, mh, mg]

# e para finalizar, será exibido qual a MAIOR e MENOR média...
for m in range(0, len(md)):
    if m == 0:
        maior = md[m]
        menor = md[m]
    else:
        if md[m] > maior:
            maior = md[m]
        if md[m] < menor:
            menor = md[m]

print(f'=> A MAIOR média foi de \033[32m{maior:.2f}\033[0;0m e a MENOR de \033[31m{menor:.2f}\033[0;0m')
print('='*30)

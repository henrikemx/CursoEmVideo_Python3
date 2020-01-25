#####################################################################
# Abelindo é um professor muito malvado. Ele quer decidir como reprovar
# Rondinelly, que tirou 8.66, 5.35, 5 e 1, respectivamente, nas provas
# P1, P2, P3 e P4. Para isso, ele pode calcular a nota final usando
# média aritmética (M.A.), média geométrica (M.G.) ou média harmônica (M.H.).
#
#   M.A. = (p1 + p2 + p3 + p4)/4
#
#   M.G. = 4V(P1 * P2 * P3 * P4)
#
#   M.H. = 4/(1/P1 + 1/P2 + 1/P3 + 1/P4)
#
# Qual dessas médias dá a maior nota pra Rondinelly? E qual das médias
# dá a pior nota?
#####################################################################

print('#'*40)
# declarando as variáveis...
p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1
maior = menor = 0

ma = (p1 + p2 + p3 + p4)/4
mg = (p1 * p2 * p3 * p4) ** (1/4)
mh = 4/(1/p1 + 1/p2 + 1/p3 + 1/p4)

print('Se as notas de Rondinelly foram, respectivamente,\n 8.66, 5.35, 5 e 1, então as médias encontradas foram...\n')
print(f'=> M.A. = {ma:.2f}\n')
print(f'=> M.G. = {mg:.2f}\n')
print(f'=> M.H. = {mh:.2f}\n')

print('#'*40)

# abaixo a lógica para identificar o MAIOR e o MENOR valores encontrados
for cnt in range(0, 3):
    if cnt == 0:
        maior = ma
        menor = ma
    else:
        if mg < ma > mh:
            maior = ma
        if mg > ma < mh:
            menor = ma
        if ma < mg > mh:
            maior = mg
        if ma > mg < mh:
            menor = mg
        if ma < mh > mg:
            maior = mh
        if ma > mh < mg:
            menor = mh

# abaixo, o resultado apresentado na tela do console...
print(f'=> Logo, a \033[32mMAIOR\033[0;0m média foi {maior:.2f} e a \033[31mMENOR\033[0;0m foi {menor:.2f}')

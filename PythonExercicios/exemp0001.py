print('Quer calcular seu IMC(Indice de massa corporal)?')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = peso/(altura*altura)
print('seu IMC é igual a: {}'.format(res))
# if (res >=16) and (res <= 26):
if 26 >= int(res) >= 16:
    print('Parabéns !')
    print('Voce está dentro da faixa ideal !')
else:
    print('Voce tem que cuidar mais de sua saúde !')
print('Sendo que o ideal é entre 16 e 26.')

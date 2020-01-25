num = int(input('Digite o numero para geração da Tabuada: '))
num1 = int(input('Fazer a contagem por quantas vezes ? '))

cont1 = 1
cont2 = 0
print('-'*20)

while (cont2 < num1):
    print('{} * {:3} = {:6}'.format(num, cont1, num*cont1))
    cont1 += 1
    cont2 += 1
print('-'*20)

# tentativa de desenvolver um programa que exiba a sequencia de Fibonacci
# resultado esperado => 0,1,1,2,3,5,8,13,21,34...

num1 = 0
num2 = 1
cnt = 0
sum = 1
cntf = int(input('Quantos termos voce deseja visualizar ?? => '))
print(0, end=', ')
while cnt < cntf:
    print(sum, end=', ')
    sum = num1 + num2
    num1 = num2
    num2 = sum
    cnt += 1
print('fim da sequencia até o {}º termo...'.format(cntf))

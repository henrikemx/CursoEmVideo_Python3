def parOuImpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
# print(parOuImpar(num))
if parOuImpar(num):
    print('O número é PAR !')
else:
    print('O número é IMPAR !')

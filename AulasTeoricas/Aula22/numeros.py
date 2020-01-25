from uteis import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O cubo de {num} é {numeros.cubo(num)}')
print(f'A raiz quadrada de {num} é {numeros.raiz(num):.4f}')

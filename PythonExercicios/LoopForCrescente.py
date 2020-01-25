par = []
impar = []

for c in range(0, 20):
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'Lista de numeros pares => {par}')

print(f'Lista de numeros ímpares => {impar}')

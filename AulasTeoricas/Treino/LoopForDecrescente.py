par = []
impar = []

for c in range(15, -1, -1):
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print()
print(f'Lista de numeros pares => {par}')
print(f'Lista de numeros ímpares => {impar}')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# programa principal
valores = [7, 2, 5, 0, 4]
print(f'Os valores originais são {valores}')
dobra(valores)
print(f'Os valores dobrados ficaram {valores}')

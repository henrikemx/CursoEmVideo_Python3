def contador1(* num):
    print(num)

def contador2(* num):
    for valor in num:
        print(f'{valor} -> ', end='')
    print('FIM')

def contador3(* num):
    tam = len(num)
    print(f'Recebi os valor {num} e são, ao todo, {tam} números')


# programa principal
contador1(5, 7, 3, 1, 4)
contador1(8, 4, 7)

print('=' * 30)

contador2(2, 4, 6, 8, 10)
contador2(1, 3, 5, 7)

print('=' * 30)

contador3(9, 7, 5, 3, 1)
contador3(0, 2, 5, 9)

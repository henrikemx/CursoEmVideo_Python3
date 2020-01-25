cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezeseis',
        'dezesete', 'dezoito', 'dezenove', 'vinte')

resp = 's'
while 's' in resp:

    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'\nVoce digitou o número {cont[num]}')

    resp = str(input('\nDeseja continuar ? [S/N] => ')).strip().lower()

print('\nFim do programa')

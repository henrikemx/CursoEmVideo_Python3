'''
Enunciado: crie um programa onde, o usuário, ao digitar uma expressão qualquer, que use parentesis. Esse programa
deverá analisar se a expressão passada está com os parentesis abertos e fechados na ordem correta.
'''

abertura = 0
fechamento = 0

texto = ['SE(A1 > A2;(A2 - A1)/A1;(A2 - A1)/A2)']

print(f'A expressão digitada foi: {texto}')

for c in texto:
    for crt in c:
        if crt in '(':
            abertura += 1
        elif crt in ')':
            fechamento += 1
if abertura == fechamento:
    print('A Expressão está correta')
elif abertura > fechamento:
    print('Falta parentesis de fechamento !')
elif abertura < fechamento:
    print('Falta parentesis de abertura !')

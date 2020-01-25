'''
Enunciado: crie um programa onde, o usuário, ao digitar uma expressão qualquer, que use parentesis. Esse programa
deverá analisar se a expressão passada está com os parentesis abertos e fechados na ordem correta.
'''

#expr = ['SE(A1 > A2;(A2 - A1/A1);(A2 - A1)/A2)']

expr = str(input('Digite a expressão: '))

print('='*30)
print(f'A expressão digitada foi: {expr}')
print('='*30)

pilha = []

for simb in expr:
    if simb in '(':
        pilha.append('(')
    elif simb in ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\nSua expressão é válida !')
else:
    print('\nSua expressão está errada !')

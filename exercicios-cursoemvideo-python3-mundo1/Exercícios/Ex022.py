#Enunciado: crie um programa que leia o nome completo de uma pessoa e mostre

#O nome com todas as letras maiusculas
#O nome com todas em minusculas
#Quantas letras ao todo (sem considerar espacos)
#Quantas letras tem o primeiro nome

nome = str(input("Informe o nome completo: ")).strip()

print('O nome completo, com todas as letras em maiuscula: {}'.format(nome.upper()))
print('O nome completo, com todas as letras e minusculo: {}'.format(nome.lower()))
print('O nome completo tem, no total, {} letras.'.format(len(''.join(nome.split()))))
print('O primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))


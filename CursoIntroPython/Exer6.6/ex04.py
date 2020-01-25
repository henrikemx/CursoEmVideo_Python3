print('='*40)
print('=> Enivaldo quer ligar três capacitores, de valores:')
print('𝐶1 = 10 𝜇F')
print('𝐶2 = 22 𝜇F')
print('𝐶3 = 6.8 𝜇F')
print('='*40)
print('Se ele ligar os três em paralelo, a capacitância resultante é a soma: 𝐶𝑝 = 𝐶1 + 𝐶2 + 𝐶3')
CapTotParal = 10 + 22 + 6.8
print('Se ele ligar os três em série, a capacitância resultante é: 1/Cs = 1/C1 + 1/C2 + 1/C3')
CapTotSerie = 1/(1/10 + 1/22 + 1/6.8)
print('Qual é o valor resultante em cada um desses casos?')
print('='*40)
print(f'=> A Capacitância total paralela é de \033[32m{CapTotParal:.3f}\033[0;0m 𝜇F')
print(f'=> A Capacitância total série é de \033[32m{CapTotSerie:.3f}\033[0;0m] 𝜇F')
print('Visualização em partes:')
p1 = 1/10
p2 = 1/22
p3 = 1/6.8
ct = p1 + p2 + p3
ctt = 1 / ct
print(f'=> 1/C1 = 1/10 = \033[32m{p1:.3f}\033[0;0m')
print(f'=> 1/C2 = 1/22 = \033[32m{p2:.3f}\033[0;0m')
print(f'=> 1/C3 = 1/6.8 = \033[32m{p3:.3f}\033[0;0m')
print(f'=> 1/C1 + 1/C2 + 1/C3 = \033[32m{ct:.3f}\033[0;0m')
print(f'=> Logo, Ctt = 1/(1/C1 + 1/C2 + 1/C3), ou seja, Ctt = \033[32m{ctt:.3f}\033[0;0m 𝜇F')
print('='*40)

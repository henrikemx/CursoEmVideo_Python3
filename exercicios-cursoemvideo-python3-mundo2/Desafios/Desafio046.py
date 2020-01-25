# Enunciado: desenvolve um programa que mostre, na tela, uma contagem
# regressive para o estouro de rojões , indo de 10 a 0, com uma pausa de 1
# segundo

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM ! BUM ! POOOOOWW !!')

# Enunciado: escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por km ultrapassado acima do limite.

velocidade = float(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print('\nVoce foi multado e terá que pagar R$ {:.2f} de multa !\nMais atenção da próxima vez !!'.format((velocidade-80)*7))
else:
    print('\nParabéns !!\nTenha um bom dia e dirija com segurança !!')

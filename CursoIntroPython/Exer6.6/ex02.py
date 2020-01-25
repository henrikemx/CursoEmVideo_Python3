print('='*40)
print('Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos,\n qual é a sua velocidade média em m/s?')
print('=> Primeiro, converter o tempo percorrido em segundos:')
h3 = (3 * 60) * 60
m23 = 23 * 60
tempTot = h3 + m23 + 17
mseg = 65000 / tempTot
print(f'03 horas = {h3} seg')
print(f'23 min = {m23} seg')
print(f'Logo, 03 horas, 23 min e 17 seg = {tempTot} seg')
print(f'=> Dividindo 65 km pelo tempo em seg, teremos {mseg:.3f} m/s')

from datetime import date
data = date.today()
print(f'Data: {data}') #2015-09-04
print(f'Dia: {data.day}') #4
print(f'Mês: {data.month}') #9
print(data.toordinal()) #735845

#Calculando 45 dias
quantidade = 45
futuro = data.fromordinal(data.toordinal() + quantidade)
print(f'Data futura: {futuro}') #2015-10-19

#Intervalo entre as datas

diferenca = futuro - data
print(f'Diferença entre datas: {diferenca}') #45 days, 0:00:00

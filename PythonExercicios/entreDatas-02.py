from datetime import datetime
from datetime import date

# Data final
d2 = datetime.strptime('2018-09-17', '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime('2017-03-07', '%Y-%m-%d')

# Calculo da quantidade de dias
print('='*30)
print(f'Data final (d2) = {d2}')
print(f'Data inicial (d1) = {d1}')
print(f'Diferença entre as datas (d1 - d2) = {d2 - d1}')
print(f'Aplicando o método days = {(d2 - d1).days}')
print(f'A média é de {abs((d2 - d1).days)}')
print('='*30)
quantidade_dias = abs((d2 - d1).days)

print(f'Decorreu cerca de {quantidade_dias} dias')
#print(f'Data atual pelo formato do sistema: {date.today()}')
#print(datetime.strptime(str(date.today()), '%Y-%m-%d'))
#print(date.weekday(date.today()))
#print(date.isoweekday(date.today()))
#print(date.ctime(date.today()))
#print(date.today())
#print(date.ctime(datetime(year=1964, month=11, day=24)))

#date1 = date.ctime(date.today())
#date2 = date.ctime(datetime(year=1964, month=11, day=24))

from _datetime import datetime

d1 = datetime(1964,11,24,3)
d2 = datetime.now()

diff = d2 - d1

print(f'Data inicial: {d1}')
print(f'Data final: {d2}')
print(f'diff: {diff}')

days = diff.days
print(f'diff.days: {days}')
years, days = days // 365, days % 365
print(f'years, days2: {years}, {days}')
months, days = days // 30, days % 30
print(f'months, days: {months}, {days}')

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print('='*30)

print(f'>> O tempo transcorrido, em segundos: {seconds} <<')
print('='*30)
print(f'>> Desde {d1} se passou <<\n => {years} anos\n => {months} meses\n => {days} dias\n => {hours} horas\n => {minutes} min. e\n => {seconds} seg.s')

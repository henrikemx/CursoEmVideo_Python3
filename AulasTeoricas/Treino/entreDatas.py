from datetime import datetime

now = datetime.now()

ano = now.year
mes = now.month
dia = now.day
hora = now.hour
min = now.minute
ds = now.tzinfo


print(f'Hoje é {dia}/{mes}/{ano} e agora é {hora}:{min} hs')
print(now.weekday())

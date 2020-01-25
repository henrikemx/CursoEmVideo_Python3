# Dica do desafio 57 do Mundo 2

sexo = str(input('Informe seu sexo: [M/F]  ')).strip().upper()[0]
cnt = 0
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida.\nPor favor, informe corretamente:  ')).strip().upper()[0]
    cnt += 1
print('Voce digitou {}. Informado corretamente !!'.format(sexo))
print('Voce fez {} tentivas sem sucesso !!'.format(cnt))
from datetime import datetime

while True:
    ano = int(input('\nInforme o ano: '))
    atual = datetime.now().year

    ano1 = ano % 4
    ano2 = ano % 100
    dif = atual - ano

    if ano1 == 0 and ano2 != 0:
        print(f'\n => O ano de {ano} foi Bissexto !!')
        print(f' => Passou {dif} anos.')
        ano3 = 28
    else:
        print(f'\n => O ano de {ano} não foi Bissexto !!')
        print(f' => Passou {dif} anos.')
        ano3 = 29

    # o loop abaixo irá retornar o total de anos, incluídos os anos bissextos
    bis = nobis = anob = anoob = 0

    for c in range(dif):
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            bis += 366
            anob += 1
        else:
            nobis += 366
            anoob += 1
        ano += 1
        if ano == atual:
            break

    tot = bis + nobis

    print(f' => Temos {anob} anos bissextos e {anoob} não bissextos')
    print(f' => Temos {bis} dias de anos bissextos e {nobis} de anos não bissextos')
    print(f' => Temos um total de {tot} dias...\n')
    print('='*30)

    resp = str(input('Deseja continuar ? [S/N] '))
    if resp in 'Nn':
        break

print(f'\n{" FIM DO PROGRAMA ":=^30}')
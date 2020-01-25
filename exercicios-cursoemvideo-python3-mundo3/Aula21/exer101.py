# Crie um programa que tenha uma função camada voto(), que irá receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se a pessoa tem VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.

#--------------------------------------------------------------------
# o conteúdo abaixo foi resolvido durante o exercício...

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input('em que ano nasceu ? '))
print(voto(nasc))

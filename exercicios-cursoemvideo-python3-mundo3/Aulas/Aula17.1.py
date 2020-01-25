num = [2, 5, 9, 1]
# tentando alterar o conteudo de um indice na tupla
# num[2] = 3
# tentando alterar o conteudo de um indice na lista
num[2] = 3
# num[4] = 7 # tentando adicionar o valor 7 ao final da lista
num.append(7) # adicionando o valor 7 ao final da lista
num.sort() # aqui o python irá ordenar de forma crescente o conteudo da lista
print(f'A) Aqui a lista é exibida na ordem crescente : {num}')
num.sort(reverse=True) # aqui a lista é exibida na ordem decrescente
print(f'B) Aqui a lista é exibida na ordem decrescente : {num}')
print(f'C) Essa lista tem {len(num)} elementos')
num.insert(2, 0)
print(f'D) Aqui foi usado o método insert para adicionar "0" na posição "2" : {num}')
num.pop()
print(f'E) Nesse exemplo, foi removido o conteudo da ultima posição da lista: {num}')
num.pop(2)
print(f'E) Nesse exemplo, foi removido o conteudo da ultima posição "2" da lista: {num}')
num.insert(2, 0)
num.append(1)
print(f'F) Restaurando a lista à sua condição anterior: {num}')
num.remove(2)
print(f'G) Nesse exemplo, foi removido o valor "2" na lista: {num}')
print(f'   * Obs.: o valor eliminado é o primeiro encontrado na busca. Quando há mais de 1 valor igual na lista')
print(f'           sugere-se o uso de laços de repetição...')
num.insert(4, 2)
print(f'H) Nesse exemplo, foi restaurado o valor "2" na posição 2 e a lista foi reordenada: {num}')
num[2] = 2
print(f'I) Nesse exemplo, foi inserido o valor "2" na posição "2": {num}')
if 4 in num:
    num.remove(4)
else:
    print(f'J) Nesse exemplo foi usado o recurso do laço para checar se o numero existe na lista.')
    print(f'    Portanto, nesse caso, o númrero 4 NÃO FOI ENCONTRADO: {num}')
if 5 in num:
    num.remove(5)
print(f'K) Nesse exemplo foi usado o recurso do laço para checar se o numero existe na lista.')
print(f'    Portanto, nesse caso, o número 5 foi removido: {num}')

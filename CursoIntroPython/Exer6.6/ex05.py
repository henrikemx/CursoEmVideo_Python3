"""
Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e
compraram alguns itens:
• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
• 2 pacotes de macarrão: R$ 8,73 cada
• 1 pacote de Molho de tomate: R$ 3,45
• 420g Cebola: R$ 5,40/kg
• 250g de Alho: R$ 30/kg
• 450g de pães franceses: R$ 25/kg

Calcule quanto ficou para cada um.
"""

cerv = 2.20
macar = 8.73
mTomate = 3.45
cebola = 5.40
alho = 30.00
paoFrances = 25.00

totCerv = 75 * cerv
totMacar = 2 * macar
totMTomate = 1 * mTomate
totCebola = 0.42 * cebola
totAlho = 0.25 * alho
totPFrances = 0.45 * paoFrances

totCompra = totCerv + totMacar + totMTomate + totCebola + totAlho + totPFrances
print('='*40)
print(f'O gasto com cada item da lista:\n')
print(f'Cerveja: \t\tR$ \033[33m{totCerv:>6.2f}\033[0;0m')
print(f'Macarrão: \t\tR$ \033[33m{totMacar:>6.2f}\033[0;0m')
print(f'Molho de tomate: \tR$ \033[33m{totMTomate:>6.2f}\033[0;0m')
print(f'Cebola: \t\tR$ \033[33m{totCebola:>6.2f}\033[0;0m')
print(f'Alho: \t\t\tR$ \033[33m{totAlho:>6.2f}\033[0;0m')
print(f'Pães franceses: \tR$ \033[33m{totPFrances:>6.2f}\033[0;0m')
print('-'*40)
print(f'TOTAL: \t\t\tR$ \033[33m{totCompra:6.2f}\033[0;0m')
print('='*40)
print(f'=> Portanto, o valor rateado entre os 4\n foi de R$ \033[33m{totCompra / 4:.2f}\033[0;0m')

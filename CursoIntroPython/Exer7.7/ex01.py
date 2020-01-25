##########################################################
# Supondo que a cotação do dólar esteja em R$ 3,25, salve
# esse valor em uma variável e utilize-o para calcular
# quanto você teria ao cambiar R$ 65,00 para dólares.
##########################################################

cotDolar = 3.25
convRealDolar = 65.00 / cotDolar
print(f'R$ 65,00 cambiado a R$ {cotDolar} resulta em US$ {convRealDolar:6.2f}')

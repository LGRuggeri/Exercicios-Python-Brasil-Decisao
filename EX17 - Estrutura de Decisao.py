# Faça um Programa que peça um número correspondente a um 
# determinado ano e em seguida informe se este ano é ou não bissexto.

import calendar

ano= int(input('Digit o ano que deseja verificar se é bissexto: '))

if calendar.isleap(ano):
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
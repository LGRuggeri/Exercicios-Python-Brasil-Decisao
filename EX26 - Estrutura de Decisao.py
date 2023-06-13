# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Álcool:

# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro 

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se 
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina= 2.5
alcool= 1.9

tipo_combustivel= input('Digite o tipo de combustível abastecido A-Álcool ou G-Gasolina: ') 
qtd_abastecido= float(input('Informe a quantidade de litros de combustível abastecido: '))

if tipo_combustivel == 'a':
    tipo_combustivel=a= 'ÁLCOOL'
else:
    tipo_combustivel=g= 'GASOLINA'


if tipo_combustivel == 'ÁLCOOL' and qtd_abastecido <= 20:
    valor_desc= ((qtd_abastecido * alcool) * 0.03)
    valor_pago= (qtd_abastecido * alcool) - valor_desc
    print(f'Foram abastecidos {qtd_abastecido} litros de {tipo_combustivel}, o valor pago de combustível foi R${valor_pago}')
elif tipo_combustivel == 'ÁLCOOL' and qtd_abastecido > 20:
    valor_desc= ((qtd_abastecido * alcool) * 0.05)
    valor_pago= (qtd_abastecido * alcool) - valor_desc
    print(f'Foram abastecidos {qtd_abastecido} litros de {tipo_combustivel}, o valor pago de combustível foi R${valor_pago}')
elif tipo_combustivel == 'GASOLINA' and qtd_abastecido <= 20:
    valor_desc= ((qtd_abastecido * alcool) * 0.04)
    valor_pago= (qtd_abastecido * alcool) - valor_desc
    print(f'Foram abastecidos {qtd_abastecido} litros de {tipo_combustivel}, o valor pago de combustível foi R${valor_pago}')
elif tipo_combustivel == 'GASOLINA' and qtd_abastecido > 20:
    valor_desc= ((qtd_abastecido * alcool) * 0.06)
    valor_pago= (qtd_abastecido * alcool) - valor_desc
    print(f'Foram abastecidos {qtd_abastecido} litros de {tipo_combustivel}, o valor pago de combustível foi R${valor_pago}')
else:
    print(f'Valores informados errados!!!')
    
    
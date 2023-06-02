# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois 
# informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque= int(input('Digite o valor de de no mínimo 10 e no máximo 600: '))


if valor_saque > 10 and valor_saque <= 600:
    resto1 = valor_saque % 100
    resto2 = resto1 % 50
    resto3 = resto2 % 10
    resto4 = resto3 % 5     
    qtd_100sacado,qtd_50sacado,qtd_10sacado,qtd_5sacado,qtd_1sacado= valor_saque//100,resto1//50,resto2//10,resto3//5,resto4//1
      

print(f'O valor de saque solicitado foi {valor_saque}')
print(f'Será fornecido {qtd_1sacado} notas de 1 real')
print(f'Será fornecido {qtd_5sacado} notas de 5 reais')
print(f'Será fornecido {qtd_10sacado} notas de 10 reais')
print(f'Será fornecido {qtd_50sacado} notas de 50 reais')
print(f'Será fornecido {qtd_100sacado} notas de 100 reais')

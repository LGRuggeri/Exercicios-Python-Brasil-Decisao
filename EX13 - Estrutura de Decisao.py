#  Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer 
# valor inválido.
 
 
dia_da_semana= int(input('Digite um número entre 1 e 7 correspondente ao dia da semana: '))

if dia_da_semana == 1:
    print('Domingo')
elif dia_da_semana == 2:
    print('Segunda')
elif dia_da_semana == 3:
    print('Terça')
elif dia_da_semana == 4:
    print('Quarta')
elif dia_da_semana == 5:
    print('Quinta')
elif dia_da_semana == 6:
    print('Sexta')
elif dia_da_semana == 7:
    print('Sábado')
else:
    print('Valor inválido.')
    
    
    
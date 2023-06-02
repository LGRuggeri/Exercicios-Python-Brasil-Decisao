# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

par_impar= int(input('Digite um número inteiro: '))

if par_impar != 0:
    par_impar= par_impar%2
    if par_impar==0:   
        print(f'O número é par')
    else:
        print((f'O número é impar'))
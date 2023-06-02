# Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer 
# as consistências, informando ao usuário nas seguintes situações:

# 1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
# 2. Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa;
# 3. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
# informe-a ao usuário;
# 4. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

valor_de_A= int(input('Digite o valor de A: '))
valor_de_B= int(input('Digite o valor de B: '))
valor_de_C= int(input('Digite o valor de C: '))

discriminante= (valor_de_B**2) - (4*(valor_de_A*valor_de_C))

# a equação possui duas soluções reais
if discriminante > 0 and valor_de_A != 0:
    raiz1= (-valor_de_B + math.sqrt(discriminante)) / (2*valor_de_A)
    raiz2= (-valor_de_B - math.sqrt(discriminante)) / (2*valor_de_A)
    print('Existem duas raizes: x1 = {0} e x2 = {1}'.format(raiz1, raiz2))
# a equação possui uma única solução real
elif discriminante == 0 and valor_de_A != 0:
    raiz1=raiz2 = -valor_de_B / (2*valor_de_A)
    print('Existem duas raizes: x1 = {0}'.format(raiz1))
# a equação não possui solução real
elif discriminante < 0 and valor_de_A != 0:
    raiz1=raiz2 = -valor_de_B / (2*valor_de_A)
    imaginaria = math.sqrt(-discriminante) / (2 * valor_de_A)  
    print('Delta menor que zero, não possui raízes reais')
else:
    print('Não é uma equação de segundo grau')

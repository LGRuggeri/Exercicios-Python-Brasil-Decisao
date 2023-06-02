# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: 
# equilátero, isósceles ou escaleno. Dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados 
# for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1= int(input('Digite o lado 1 do triângulo: '))
lado2= int(input('Digite o lado 2 do triângulo: '))
lado3= int(input('Digite o lado 3 do triângulo: '))

if lado1+lado2 > lado3:
    if lado1==lado2==lado3:
        print('É um Triângulo Equilátero')
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print('É um Triângulo Isósceles')
    elif lado1 != lado2 != lado3:
        print('É um Triângulo Escaleno')
    
    
else:
    print('Não é um Triângulo')
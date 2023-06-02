# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento. 
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação 
# ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase 
# que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


n= float(input('Digite o 1 número: '))
n2= float(input('Digite o 2 número: '))
operacao= input('Qual operação deseja fazer SOMA(+), SUBTRAÇÃO(-), DIVISÃO(/) ou MULTIPLICAÇÃO(*): ')


if operacao== '+':
    soma= n+n2
    if soma > 0:
        soma= round(soma%2,2)
        if soma == 0:
            print('O número é par, Positivo e Inteiro')
        else: 
            print('O número é impar, Positivo e decimal')
    else:
        print('Valor zerado')
                

if operacao== '-':
    sub= n-n2
    if sub > 0:
        sub= round(sub%2,2)
        if sub == 0:
            print('O número é Par, Positivo e Inteiro')
        else: 
            print('O número é Impar, Positivo e Decimal')
    elif sub < 0:
        sub= round(sub%-2,2)
        if sub == 0:
            print('O número é Par, Negativo e Inteiro')
        else: 
            print('O número é Impar, Negativo e Decimal')
    else:
        print('Valor zerado')   
        
if operacao== '/':
    div= n/n2
    if div != 0:
        div= round(div%2,2)
        if div == 0:
            print('O número é Par, Positivo e Inteiro')
        else: 
            print('O número é Impar, Positivo e Decimal')
    else:
        print('Valor zerado')  
        
if operacao== '*':
    multp= n*n2
    print(multp)
    if multp > 0:
        multp= round(multp%2,2)
        if multp == 0:
            print('O número é par, Positivo e Inteiro')
            print(multp)
        else: 
            print('O número é impar, Positivo e decimal')
            print(multp)
    elif multp < 0:
        multp= round(multp%-2,2)
        if multp == 0:
            print('O número é Par, Negativo e Inteiro')
        else: 
            print('O número é Impar, Negativo e Decimal')
    else:
        print('Valor zerado')
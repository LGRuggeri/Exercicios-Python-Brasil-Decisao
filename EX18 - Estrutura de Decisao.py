# Faça um Programa que peça uma data no formato dd/mm/aaaa e 
# determine se a mesma é uma data válida.

data = input("Digite a data no seguinte modelo: [dd/mm/aaaa] :")
if len(data) != 10:
    print('Data inválida')
else:
    if data[2] != '/' or data[5] != '/':
        print('Data inválida')
    else:
        numeros_data = data.split('/')
        if int(numeros_data[0]) > 31:
            print('Data inválida')
        elif int(numeros_data[1]) > 12:
            print('Data inválida')
        else:
            print('Data válida')
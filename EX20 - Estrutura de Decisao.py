# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:

# A mensagem "Aprovado", se a média for maior ou igual a 7, 
# com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, 
# com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

import math

def media():
    n1= float(input('Digite 1 nota do aluno:'))
    n2= float(input('Digite 2 nota do aluno:'))
    n3= float(input('Digite 3 nota do aluno:'))
    
    media= round((n1 + n2 + n3) / 3,2)
    
    if media == 10:
        print(f'Aprovado com Distinção {media}')
    elif media >= 7 and media < 10:
        print(f'Aprovado {media}') 
    else:
        print(f'Reprovado {media}') 
        
        
media()
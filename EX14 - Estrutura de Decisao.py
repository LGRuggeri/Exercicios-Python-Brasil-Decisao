# Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
# disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento

# Entre 9.0 e 10.0 : A
# Entre 7.5 e 9.0 : B
# Entre 6.0 e 7.5 : C
# Entre 4.0 e 6.0 : D
# Entre 4.0 e zero : E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito 
# for D ou E.

conceito= ['A','B','C','D','E']

n1= float(input('Digite a 1 nota do aluno: '))
n2 = float(input('Digite a 2 nota do aluno: '))

media= (n1 + n2) / 2


if media > 9.0 and media <= 10.0:
    print('Sua média foi',media,'seu aproveitamento foi',conceito[0],'você foi "APROVADO"')
elif media > 7.5 and media <= 9.0:
    print('Sua média foi',media,'seu aproveitamento foi',conceito[1],'você foi "APROVADO"')
elif media > 6.0 and media <= 7.5:
    print('Sua média foi',media,'seu aproveitamento foi',conceito[2],'você foi "APROVADO"')
elif media > 4.0 and media <= 6.0:
    print('Sua média foi',media,'seu aproveitamento foi',conceito[3],'você foi "REPROVADO"')
elif media >= 0 and media <= 4.0 :
    print('Sua média foi',media,'seu aproveitamento foi',conceito[4],'você foi "REPROVADO"')

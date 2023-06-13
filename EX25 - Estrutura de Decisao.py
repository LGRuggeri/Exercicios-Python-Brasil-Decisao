# 24. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação 
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

positivos=0

tel_vitima= int(input('Telefonou para a vítima? 1)Sim ou 2)Não: '))
local_vitima= int(input('Esteve no local do crime? 1)Sim ou 2)Não: '))
mora_vitima= int(input('Mora perto da vítima? 1)Sim ou 2)Não: '))
devia_vitima= int(input('Devia para a vítima? 1)Sim ou 2)Não: '))
trabalhou_vitima= int(input('Já trabalhou com a vítima? 1)Sim ou 2)Não: '))

if tel_vitima==1:
    positivos+= 1
else:
    print('Não telefonou para a vitíma')
if local_vitima==1:
    positivos+= 1
else:
    print('Não esteve no local do crime')
if mora_vitima==1:
    positivos+= 1
else:
    print('Não mora próximo da vitíma')
if devia_vitima==1:
    positivos+= 1
else:
    print('Não devia para a vitíma')
if trabalhou_vitima==1:
    positivos+= 1
else:
    print('Não trabalhou com a vitíma')
    
    
if positivos<2:
    print('\nVocê tem 0 afirmações positivas, é inocente!')
elif positivos==2:
    print('\nVocê tem 2 afirmações positivas, é suspeito(a) do assassinato!')
elif positivos<5:
    print('\nVocê tem 3 há 4 afirmações positivas, é cúmplice do assassinato!')
else:
    print('\nVocê tem 5 afirmações positivas, é o assassino!')

    
  
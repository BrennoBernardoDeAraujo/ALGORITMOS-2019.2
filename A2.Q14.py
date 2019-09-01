
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
#"Já trabalhou com a vítima?
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#  entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

auxC = 0
resp = input("Telefonou para a vítima?")
if resp == "sim": 
    auxC = auxC + 1 
    if resp != "sim":
        auxC = auxC + 0
resp = input("Esteve no local do crime?") 
if resp == "sim":
    auxC = auxC + 1 
    if resp != "sim":
        auxC = auxC + 0
resp = input("Mora perto da vítima?")
if resp == "sim":
    auxC = auxC + 1
    if resp != "sim":
        auxC = auxC + 0
resp = input("Devia para a vítima?")
if resp == "sim":
    auxC = auxC + 1
    if resp != "sim":
        auxC = auxC + 0
resp = input("Já trabalhou com a vítima?")
if resp == "sim":
    auxC = auxC + 1
    if resp != "sim":
        auxC = auxC + 0
if auxC == 2:
    print("Suspeito")
if auxC == 3 or auxC == 4:
    print("Cúmplice")
if auxC == 5:
    print("Assassino")
if auxC == 0:
    print("Inocente")
# 6. Faça um programa que calcula o novo valor do salário de um funcionário.
# O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

SA = float (input("Salário atual: "))
R = float (input("percentual do reajuste: "))
NS = float (SA * (1 + (R / 100)))
print ("o novo valor do salário é: ",NS)

# Siginificado das siglas:

# SA = Salário atual
# R  = percentual do reajuste
# NS = novo valor do salário
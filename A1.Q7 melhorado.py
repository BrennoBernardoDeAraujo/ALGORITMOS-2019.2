# 7. Faça um programa que calcula o tempo (em anos) que uma pessoa irá demorar para
# poupar R$ 1.000.000,00 (Um Milhão de Reais). O usuário informa o salário mensal e o total
# de despesas mensais.

SM = float (input("Salário mensal: "))
DM = float(input("Despesas mensais: "))
AnosQF = float (1000000/(SM - DM)/12)
print ("O tempo (em anos) que  irá demorar para poupar Um Milhão de Reais é: ", AnosQF)

# Siginificado das siglas:

# SM = Salário mensal
# DM = Despesas mensais
# AnosQF = O tempo (em anos) que  irá demorar para poupar Um Milhão de Reais
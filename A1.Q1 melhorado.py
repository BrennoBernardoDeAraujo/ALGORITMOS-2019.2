# 1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e
# quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o
# usuário obterá com esses valores.

VL = float(input("Valor do litro de combustível: "))
VA = float(input("Valor que deseja abastecer: "))
QL = float(VA / VL)
print ("Quantidade de litros abastecidos: ",QL)

# Siginificado das siglas:

# VL = Valor do litro de combustível
# VA = Valor que deseja abastecer
# QL = Quantidade de litros abastecidos
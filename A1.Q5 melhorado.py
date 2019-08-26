# 5. Faça um programa que calcule a conversão monetária de Real para Dólar. O usuário
# informa o valor da cotação do dólar (ex.: 3,78) e quanto em real deseja converter (ex.150,00).
# O programa exibe quantos dólares valem os reais informados.

CD = float(input("Cotação do dólar: "))
QR = float(input("Quanto em reais deseja converter: "))
QD = float (QR / CD)
print ("A quantidade de reais informados equivalem em dólares a: ",QD)

# Siginificado das siglas:

# CD = Cotação do dólar
# QR = Quanto em reais deseja converter
# QD = Quantidade de  dólares que valem os reais informados
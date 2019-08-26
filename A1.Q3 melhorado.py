# 3. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário
# deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso 
#(ex.35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

D = float(input("valor original da dívida : "))
A = float(input("quantidade de dias em atraso: "))
M = float(input("valor da multa por dia de atraso : "))
T = float (D + (A*M))
print ("valor total a ser pago pela dívida em atraso: ",T)

# Siginificado das siglas:

# D = valor original da dívida
# A = quantidade de dias em atraso
# M = valor da multa por dia de atraso
# T = valor total a ser pago pela dívida em atraso
# 2. Faça um programa que calcule a média de consumo de combustível de um veículo. O
# usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros
# foram gastos no percurso.

I = float (input("Quilometro inicial: "))
F = float (input("Quilometro final: "))
L = float (input("Litros gastos: "))
S = float (F - I)
C = float (S / L)
print ("A média de consumo de combustível do veículo é: ",C)

# Siginificado das siglas:

# I = Quilometro inicial
# F = Quilometro final
# L = Litros gastos no trajeto
# S = Distncia percorrida
# C = Consumo médio do veículo 
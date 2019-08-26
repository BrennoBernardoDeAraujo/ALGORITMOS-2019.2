#4. Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário
# deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de
# cada um e por fim exibir a área total da casa.

CC1 = float(input("Comprimento do cômodo 1: "))
LC1 = float(input("lagura do cômodo 1: "))
CC2 = float(input("Comprimento do cômodo 2: "))
LC2 = float(input("lagura do cômodo 2: "))
CC3 = float(input("Comprimento do cômodo 3: "))
LC3 = float(input("lagura do cômodo 3: "))
CC4 = float(input("Comprimento do cômodo 4: "))
LC4 = float(input("lagura do cômodo 4: "))
A1 =  float (CC1 * LC1)
A2 =  float (CC2 * LC2)
A3 =  float (CC3 * LC3)
A4 =  float (CC4 * LC4)
AT =  float (A1 + A2 + A3 + A4)
print ("Área total da casa em metros quadrados: ",AT)

# Siginificado das siglas:

# CC1 = Comprimento do cômodo 1
# LC1 = lagura do cômodo 1
# CC2 = Comprimento do cômodo 2
# LC2 = lagura do cômodo 2
# CC3 = Comprimento do cômodo 3
# LC3 = lagura do cômodo 3
# CC4 = Comprimento do cômodo 4
# LC4 = lagura do cômodo 4
# A1 =  Área do cômodo 1
# A2 =  Área do cômodo 2
# A3 =  Área do cômodo 3
# A4 =  Área do cômodo 4
# AT =  Área total da casa
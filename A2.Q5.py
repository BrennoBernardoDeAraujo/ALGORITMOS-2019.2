# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

n1 = float(input("Cachaça Matuta Lata 270Ml : "))
n2 = float(input("CERVEJA ITAIPAVA LITRINHO 300ML: "))
n3 = float(input("Cachaça 51 Lata 350mL : "))

if n1 <= n2 and n1 <= n3:
    print("Você deve comprar Cachaça Matuta Lata 270Ml")
if n2 <= n1 and n2 <= n3:
    print("Você deve comprar CERVEJA ITAIPAVA LITRINHO 300ML")
if  n3 <= n1 and n3 <= n2:
    print("Você deve comprar CERVEJA ITAIPAVA LITRINHO 300ML")
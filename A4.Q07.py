"""
A04.Q007 -  Um programa que desenhe um triângulo retângulo com a base voltada para cima, como a
seguir:

****************
**************
************
**********
********
******
****
**

"""
ch = input("Caractere: ")

for linha in range(8):
    for coluna in range(8-linha):
        print(ch, sep = '', end = '')
    print()
        

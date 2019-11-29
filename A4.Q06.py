"""
A04.Q005 -  Um programa que desenhe um triângulo retângulo com a base voltada para baixo, comoa seguir:

*
**
***
****
*****
******
*******
********

"""
ch = input("Caractere: ")
for linha in range(-8,1):
    for coluna in range(8+linha):
        print(ch, sep='', end='')
    print()

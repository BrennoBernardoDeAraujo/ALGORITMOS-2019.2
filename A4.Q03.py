"""
Para as questões 3 a 7, rode o programa a seguir:

ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            print(ch, ch, sep = '', end = '')
            else:
        print(' ', sep = '', end = '')
    print()


Procure entender a lógica deste programa e, em seguida, partindo do mesmo, implemente:

A04.Q003 -  Um programa que desenhe um quadrado totalmente preenchido, como a seguir:"""

ch = input("Caractere: ")

for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0 :
            print(ch,ch, sep='', end='')
        else:
            print(end='')
    print()

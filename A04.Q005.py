"""
A04.Q005 -  Um programa que desenhe a diagonal principal e a diagonal secundária do quadrado,como a seguir:

**            **
  **        **
    **    **
      ****
      ****
    **    **
  **        **
**            **

"""

ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if linha == coluna or (linha + coluna) == 7:
            print(ch, ch, sep='', end='')
        else:
            print(' ',' ',sep='', end='')
    print()

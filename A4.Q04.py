"""
A04.Q004 - Um programa que desenhe a diagonal principal do quadrado, como a seguir:
**
   **
      **
         **
            **
               **
                  **
                     **
"""

ch = input("Caractere: ")

for linha in range(8):
    for coluna in range(8):
        if linha == coluna:
            print(f'{ch}{ch}', sep='', end='')
        else:
            print('   ',sep='',end='')
    print()

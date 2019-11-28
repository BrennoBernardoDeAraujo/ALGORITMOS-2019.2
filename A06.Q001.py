"""
1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""

ordem = int(input('matriz ordem'))


def criando_matriz():
    matriz = []
    for i in range(ordem):
        matriz.append([0]*ordem)
    return matriz


executarMatriz = criando_matriz()
contador = 0


for i in range(4):
    for j in range(4):
        executarMatriz[i][j] = int(
            input(f'Digite um elemento correspondente a matriz [{str(i+1)}][{str(j+1)}] '))
        if executarMatriz[i][j] > 10:
            contador += 1

for i in range(4):
    for j in range(4):
        print(executarMatriz[i][j], end=" ")
    print()
print(f'A matriz possui {contador} valores maiores que 10')

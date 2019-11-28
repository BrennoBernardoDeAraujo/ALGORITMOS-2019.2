"""
A06.Q003 -  Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas.
"""
def cria_matriz():
    matriz = []
    for i in range(4):
        matriz.append([0]*4)
    return matriz


primeira_matriz = cria_matriz()
segunda_matriz = cria_matriz()
terceira_matriz = cria_matriz()

print(f'Digite os valores da primeira matriz.')
for i in range(4):
    for j in range(4):
        primeira_matriz[i][j] = int(
            input(f'Digite os elementos [{str(i+1)}][{str(j+1)}]: '))

print(f'Digite os valores da segunda matriz.')
for i in range(4):
    for j in range(4):
        segunda_matriz[i][j] = int(
            input(f'Digite os elementos [{str(i+1)}][{str(j+1)}]: '))

for i in range(4):
    for j in range(4):
        if primeira_matriz[i][j] > segunda_matriz[i][j]:
            terceira_matriz[i][j] = primeira_matriz[i][j]
        else:
            terceira_matriz[i][j] = segunda_matriz[i][j]

print(f'Resultado:')
for i in range(4):
    for j in range(4):
        print(terceira_matriz[i][j], end=' ')
    print()

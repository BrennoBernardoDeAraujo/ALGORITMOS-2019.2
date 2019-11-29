"""
A06.Q004 -  Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da
forma:
  a. A[i][j] = 2i + 7j − 2 se i < j;
  b. A[i][j] = 3i
  2 − 1 se i = j;
  c. A[i][j] = 4i
  3 − 5j
  2 + 1 se i > j.                              """


def criando_matriz():
    matriz = []
    for i in range(10):
        matriz.append([0]*10)
    return matriz


elemento_matriz = cria_matriz()

for i in range(10):
    for j in range(10):
        if i < j:
            elemento_matriz[i][j] = 2*i+7*j-2
        elif i == j:
            elemento_matriz[i][j] = 3*(i**2)-1
        else:
            elemento_matriz[i][j] = (4*(i**3))-5

print(f'Resultado:')
for i in range(10):
    for j in range(10):
        print(elemento_matriz[i][j], end=' ')
    print()

"""
A06.Q005 -  Leia uma matriz de ordem n, informada pelo usuário. Calcule a soma dos elementos que estão acima da diagonal principal."""

ordem = int(input('Digite a ordem da matriz: '))


def cria_matriz():
    matriz = []
    for i in range(ordem):
        matriz.append([0]*ordem)
    return matriz


elemento_matriz = cria_matriz()
resultado = 0

for i in range(ordem):
    for j in range(ordem):
        elemento_matriz[i][j] = int(
            input(f'Digite os elementos [{str(i+1)}][{str(j+1)}]: '))
        if j > i:
            resultado = resultado + elemento_matriz[i][j]
print(
    f'O resultado da soma do diagonal principal da matriz é: {resultado} ')

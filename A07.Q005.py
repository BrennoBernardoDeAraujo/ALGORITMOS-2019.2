'''
A07.Q005 - Considere duas matrizes quadradas de ordem N. 
solicite uma linha e uma coluna e troque os valores da posição correspondente entre as matrizes.
Imprima as duas matrizes antes e depois da troca. '''


def criar_matriz(ordem):
   matriz = []
   for i in range(ordem):
    matriz.append([0]*ordem)
    return matriz

def ler_matriz(matriz,ordem):
    for i in range(ordem):
        for j in range(ordem):
            matriz[i][j] = int(input("Matriz Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))
    return matriz
def troca(matriz1,matriz2,ordem):
    aux1=0
    while aux1 == 0:
        aux=0
        linha=int(input('Digite a linha para fazer a troca :'))
        coluna=int(input('Digite a coluna para fazer a troca :'))
        aux=matriz1[linha-1][coluna-1]
        matriz1[linha-1][coluna-1] = matriz2[linha-1][coluna-1]    
        matriz2[linha-1][coluna-1] = aux
        aux1+=1


def print_matriz(matriz,ordem):
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end = " ")
        print()

ordem = int(input('Digite a ordem da matriz: '))



matriz=criar_matriz(ordem)
print('MATRIZ 1')

matriz1=ler_matriz(matriz,ordem)
aux=matriz1
print()

matriz=criar_matriz(ordem)
print('MATRIZ 2')

matriz2=ler_matriz(matriz,ordem)
print()

print('MATRIZ 1')
print_matriz(matriz1,ordem)
print()

print('MATRIZ 2')
print_matriz(matriz2,ordem)
print()


troca(matriz1,matriz2,ordem)
print()
print('MATRIZ 1 DEPOIS DA TROCA')
print_matriz(matriz1,ordem)
print()

print('MATRIZ 2 DEPOIS DA TROCA')
print_matriz(matriz2,ordem)

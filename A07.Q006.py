'''
A07.Q007 - Faça um programa que leia uma matriz de dimensões informadas pelo usuário. Dado um valor, 
verifique quantas vezes algum múltiplo desse valor aparece na matriz.'''

def criar_matriz(linha,coluna):
    matriz0=[]
    for i in range(linha):
        matriz0.append([0]*coluna)
    return matriz0

def ler_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j]=int(input('matriz [ '+str(i+1)+'] ['+str(j+1)+' ]'))


def multiplo(linha,coluna,matriz,num):
    cont=0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] % num == 0:
                cont+=1
    return cont



def print_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()


linha = int(input('Digite um número para quantidade de linhas para a matriz : '))
coluna = int(input('Agora um número para as colunas : '))

matriz = criar_matriz(linha,coluna)
ler_matriz(matriz,linha,coluna)


num = int(input('digite um nÚmero para saber seu multiplo na matriz : '))

aux=multiplo(linha,coluna,matriz,num)
print('MATRIZ')
print_matriz(matriz,linha,coluna)

print( aux,'múltiplos')
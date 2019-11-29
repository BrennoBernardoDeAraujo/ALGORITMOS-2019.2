'''
A07.Q007 - Faça um programa que leia uma matriz de dimensões informadas pelo usuário. Dado um valor, 
verifique quantas vezes algum múltiplo desse valor aparece na matriz.'''

NdeC = int(input('Digite o número de colunas da matriz: '))
NdeL = int(input('Digite o número de linhas da matriz: '))

def gerar_matriz_0(NC,NL):
    MATRIZ = []
    for i in range(NL):
        MATRIZ.append([0] * NC)
    return MATRIZ

MATRIZ_ZERADA = gerar_matriz_0(NdeC,NdeL)

def gerar_matriz_U(MATRIZ,NC,NL):
    MATRIZ_U = MATRIZ
    for i in range(NL):
       for j in range(NC):
            p1 = i + 1
            p2 = j + 1
            MATRIZ_U[i][j] = input('Digite o numero de posiçao '+ str(p1)+','+ str(p2) + ' na matriz: ')
    return MATRIZ_U

MATRIZ_USUÁRIO = gerar_matriz_U(MATRIZ_ZERADA,NdeC,NdeL)
VALOR = input('Digite um valor: ')

def QdeMÚLTIPLOS(MATRIZ,NC,NL,V):
    QdeM = 0
    V2 = int(V)
    MATRIZ_C = []
    MATRIZ_C = MATRIZ
    for i in range(NL):
        for j in range(NC):
            if int(MATRIZ_C[i][j]) % V2 == 0:
                QdeM += 1
    return  QdeM

QdeQdeMÚLTIPLOS = QdeMÚLTIPLOS(MATRIZ_USUÁRIO,NdeC,NdeL,VALOR)
print()
print('A quantidade de múltiplos de '+ str(VALOR) + ' na matriz é ' + str(QdeQdeMÚLTIPLOS))

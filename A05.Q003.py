'''
A05.Q003 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. '''

NdeC = 10
print()
vetor = []



def gerarVetor(VET,NC):
    VET = []
    VET = [0] * NC
    for i in range(NC):
        Iatual = int(i + 1)
        VET[i] = int(input('Digite o item '+ str(Iatual) + ' do vetor: '))
    return VET

vetor = gerarVetor(vetor,NdeC)


def separar_Npares(VET):
    NC_VET = len(VET)                       # Número de colunas do VET
    VET_pares = []
    for i in range(NC_VET):
        if VET[i] % 2 == 0:
           VET_pares.append(VET[i])
    return VET_pares

Npares_vetor = separar_Npares(vetor)
Qpares = len(Npares_vetor)

print()
print("O vetor possui " + str(Qpares) + " valores pares!" )
print()
print("Os valores pares sao:",Npares_vetor)
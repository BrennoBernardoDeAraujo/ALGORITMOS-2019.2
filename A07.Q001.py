# A07.Q1 - Faça um programa que leia um vetor de inteiros. 
# Imprima separadamente os valores pares e os valores ímpares do vetor.

utilidade_programa = 'Separador de números ímpares e pares de vetores'  

print('-=' * (len(utilidade_programa) + 8))
print()
print(' ' * 4,utilidade_programa,' ' * 4 )
print()
print('-=' * (len(utilidade_programa) + 8))

NdeC = int(input('Digite o número de colunas do vetor: '))
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


def separar_Nímpares(VET):
    NC_VET = len(VET)                       # Número de colunas do VET
    VET_ímpares = []
    for i in range(NC_VET):
        if VET[i] % 2 != 0:
           VET_ímpares.append(VET[i])
    return VET_ímpares

Npares_vetor = separar_Npares(vetor)

Nímpares_vetor = separar_Nímpares(vetor)

print()
print('Os números pares do vetor: ',Npares_vetor )
print()
print('Os números ímpares do vetor: ',Nímpares_vetor )
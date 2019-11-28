'''
A07.Q003 - Dado um vetor de tamanho N, inverta a ordem de seus elementos e imprima o vetor resultante. '''

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

def inverter_V(VET):
    NC = len(VET)
    VET_I = []
    VET_I = [0] * NC
    for i in range(NC):
            VET_I[i] = VET[NC - 1 - i]
    return VET_I

vetor_inv = inverter_V(vetor)

print()
print(vetor_inv)

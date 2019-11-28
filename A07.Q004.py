'''
A07.Q004 - Dado um vetor, de tamanho N, de valores inteiros, 
verifique se os elementos nele contidos encontram-se em ordem crescente. '''

NdeC = int(input('Digite o número de colunas dos vetores: '))
print()
vetor = []

def gerarVetor(VET,NC):
    VET = []
    VET = [0] * NC
    for i in range(NC):
        Iatual = int(i + 1)
        VET[i] = str(input('Digite o item '+ str(Iatual) + ' do vetor: '))
    return VET

vetor = gerarVetor(vetor,NdeC)

def vef_ordem_cresc_V(VET):
    NC = len(VET)
    for i in range(NC - 1):
        if VET[i] > VET[i + 1]:
            return 'Nao está em ordem crescente'
    return 'Está em ordem crescente'

MSG = vef_ordem_cresc_V(vetor)
print()
print(MSG)

        
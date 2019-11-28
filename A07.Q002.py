'''
A07.Q002 - Faça um programa que leia um vetor de caracteres de tamanho N, 
contendo as respostas de um candidato em uma prova de concurso. 
A seguir, leia outro vetor, dessa vez contendo o gabarito da prova. 
Gere um terceiro vetor, de booleanos, indicando os erros e acertos do candidato. 
Com base nesse vetor, imprima o percentual de questões acertadas pelo candidato. '''



NdeC = int(input('Digite o número de colunas dos vetores: '))
print()
vetor_resposta = []
vetor_gabarito = []

def gerarVetor(VET,NC):
    VET = []
    VET = [0] * NC
    for i in range(NC):
        Iatual = int(i + 1)
        VET[i] = str(input('Digite o item '+ str(Iatual) + ' do vetor: '))
    return VET

print('Digite as respostas: ')
vetor_resposta = gerarVetor(vetor_resposta,NdeC)

print()
print('Digite o gabarito: ')
vetor_gabarito = gerarVetor(vetor_gabarito,NdeC)

def verificar_Iiguais(VET1,VET2):
    NC_VET = len(VET1)
    VET_bool = []
    for i in range(NC_VET):
        if VET1[i] == VET2[i]:
            VET_bool.append(bool(VET1[i] == VET2[i]))
        else: 
            VET_bool.append(bool(VET1[i] == VET2[i]))
    return VET_bool

vetor_booleano = verificar_Iiguais(vetor_resposta,vetor_gabarito)

def percentual_FT(VET):
    NC_VET = len(VET)
    QT = 0
    QF = 0
    for i in range(NC_VET):
        if VET[i] == True:
           QT += 1
        else: 
           QF += 1
    return str(( QT / NC_VET) * 100)

perc_Q_acertadas = percentual_FT(vetor_booleano)
print()
print('O percentual de questões acertadas pelo candidato foi: '+ perc_Q_acertadas + '%')
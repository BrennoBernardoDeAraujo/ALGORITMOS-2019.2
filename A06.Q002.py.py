"""
Aluno: Luan dos Santos Rodrigues
Matricula: 192810286
Curso: Bacharelado em Computação - UEPB
Cadeira: Algoritmos 2019.2
Turno: Manhã
Prof. Ricardo Oliveria 

2. Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma
busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.

"""


def criando_matriz():
    matriz = []
    for i in range(5):
        matriz.append([0]*5)
    return matriz


executar_matriz = criando_matriz()

verificar = int(input('Digite o valor que você deseja verificar: '))
verificar_posicao = []

for i in range(5):
    for j in range(5):
        executar_matriz[i][j] = int(
            input(f'Digite os elementos da matriz [{str(i+1)}][{str(j+1)}] '))
        if executar_matriz[i][j] == verificar:
            list.append(verificar_posicao, [i+1, j+1])

if verificar_posicao == []:
    print('Valor invalido!')
else:
    print(f'O valor verificado está presente na posição {verificar_posicao}')

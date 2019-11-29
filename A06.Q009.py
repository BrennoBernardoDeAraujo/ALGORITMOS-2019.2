"""
A06.Q009 - Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltipla escolha, referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a pontuação correspondente a cada aluno."""

matriz = []
for i in range(5):
    matriz.append([0]*10)

for i in range(5):
    for j in range(10):
        matriz[i][j] = int(
            input(f'Resposta do Aluno: [{str(i+1)}] Questões: [{str(j+1)}]: '))
        while matriz[i][j] != 'a' and matriz[i][j] != 'b' and matriz[i][j] != 'c' and matriz[i][j] != 'd':
            print('Resposta invalida, tente novamento!')
            matriz[i][j] = input(
                f'Professor, qual a resposta correta da questão []')

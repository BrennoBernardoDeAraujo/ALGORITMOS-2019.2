"""
A05.Q005 - Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes.
A prova consta de 10 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
  ● o cartão gabarito;
  ● o número de alunos da turma;
  ● o cartão de respostas para cada aluno, contendo o seu número e suas respostas.."""

alunos = int(input('Digite a quantiadade de alunos: '))
questoes = [0]*10
gabarito = [0]*10
acertos = 0


for resposta in range(10):
    questoes[resposta] = input(f'Resposta das questões: ')


for r in range(10):
    questoes[r] = str(input('Resposta das questões: '))
for i in range(alunos):
    acertos = 0
    print(f'Insira a resposta do aluno {i+1}')
    for j in range(10):
        questao = str(input('Resposta: '))
        if questao[j] == gabarito[i]:
            acertos = acertos + 1
    print(f'Aluno {i} acertou {acertos} questões!')

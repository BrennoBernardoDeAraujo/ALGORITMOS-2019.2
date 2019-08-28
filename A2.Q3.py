# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem “Prova Final”, se a média alcançada estiver entre cinco e sete;
# A mensagem "Reprovado", se a média for menor do que sete

n1 = float (input("primeira nota: "))
n2 = float (input("segunda nota: "))
m = float (n1 + n2)/ 2

if  m >= 7:
  print ("Aprovado")
elif  m >= 5:
  print ("Prova Final")
else: 
  print ("Reprovado")
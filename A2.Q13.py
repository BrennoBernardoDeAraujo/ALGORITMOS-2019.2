# 13.Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque
# e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 
# duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
# três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

Vsaque = int(input("Valor do saque: "))
centena = int(Vsaque/100)
dezena = int((Vsaque -(centena*100))/10)
unidade = int(Vsaque - (centena*100 + dezena*10))
notas100 = centena
notas50 = 0
notas10 = dezena
notas5 = 0
notas1 = unidade
if Vsaque < 10 or Vsaque > 600:
    print("valor nao permitido,valor minimo 10 e maximo de 600")
if dezena > 5:
    notas50 =  1  
    notas10 = dezena - 5
    if unidade > 5 and (Vsaque >= 10 or Vsaque <= 600):
        notas5 =  1 
        notas1 = unidade - 5
    if notas100 > 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas100,"notas de 100 ,",end="")
    if notas100 == 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas100,"nota de 100 ,",end="")
    if notas50 > 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas50,"notas de 50 ,",end="")
    if notas50 == 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas50,"nota de 50 ,",end="")
    if notas10 > 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas10,"notas de 10 ,",end="")
    if notas10 == 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas10,"nota de 10 ",end="")
    if notas5 > 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas5,"notas de 5 ,",end="")
    if notas5 == 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas5,"nota de 5 ,",end="")
    if notas1 >= 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas1,"notas de 1 .",end="")
    if notas10 == 1 and (Vsaque >= 10 or Vsaque <= 600):
        print(notas1,"nota de 1 .",end="")